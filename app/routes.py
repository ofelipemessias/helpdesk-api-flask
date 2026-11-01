from flask import Blueprint, jsonify, request

from .models import VALID_PRIORITIES, VALID_STATUSES, Ticket, db

tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.get("/tickets")
def list_tickets():
    query = Ticket.query
    status = request.args.get("status")
    if status:
        if status not in VALID_STATUSES:
            return jsonify({"error": "invalid status filter"}), 400
        query = query.filter_by(status=status)
    tickets = query.order_by(Ticket.created_at.desc()).all()
    return jsonify([t.to_dict() for t in tickets]), 200


@tickets_bp.post("/tickets")
def create_ticket():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    priority = data.get("priority", "medium")
    if priority not in VALID_PRIORITIES:
        return jsonify({"error": "invalid priority"}), 400
    ticket = Ticket(
        title=title,
        description=data.get("description", ""),
        priority=priority,
    )
    db.session.add(ticket)
    db.session.commit()
    return jsonify(ticket.to_dict()), 201


@tickets_bp.get("/tickets/<int:ticket_id>")
def get_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    if ticket is None:
        return jsonify({"error": "ticket not found"}), 404
    return jsonify(ticket.to_dict()), 200


@tickets_bp.patch("/tickets/<int:ticket_id>")
def update_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    if ticket is None:
        return jsonify({"error": "ticket not found"}), 404
    data = request.get_json(silent=True) or {}
    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({"error": "invalid status"}), 400
        ticket.status = data["status"]
    if "priority" in data:
        if data["priority"] not in VALID_PRIORITIES:
            return jsonify({"error": "invalid priority"}), 400
        ticket.priority = data["priority"]
    if "title" in data:
        title = (data["title"] or "").strip()
        if not title:
            return jsonify({"error": "title cannot be empty"}), 400
        ticket.title = title
    if "description" in data:
        ticket.description = data["description"]
    db.session.commit()
    return jsonify(ticket.to_dict()), 200


@tickets_bp.delete("/tickets/<int:ticket_id>")
def delete_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    if ticket is None:
        return jsonify({"error": "ticket not found"}), 404
    db.session.delete(ticket)
    db.session.commit()
    return "", 204
