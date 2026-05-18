from ringmaster.dialogue import DialogueContext, DialogueEngine


def test_positive_respectful_reply_improves_relationship() -> None:
    ctx = DialogueContext(sender="Head Writer", topic="tonight's main event", relationship=55, urgency=50)
    out = DialogueEngine().respond(ctx, "Thanks, please proceed with that plan.")
    assert out.relationship_delta > 0
    assert "align" in out.reply.lower() or "proceed" in out.reply.lower()


def test_negative_demanding_reply_hurts_relationship() -> None:
    ctx = DialogueContext(sender="Top Star", topic="entrance budget", relationship=65, urgency=80)
    out = DialogueEngine().respond(ctx, "No, do it now, this is ridiculous")
    assert out.relationship_delta < 0
    assert "need to revisit" in out.reply.lower()
