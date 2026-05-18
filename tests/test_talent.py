from pathlib import Path

from ringmaster.talent import TalentPool, TalentTrainer


def test_load_free_agents() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    agents = TalentPool.load_free_agents(repo_root)
    assert len(agents) >= 3
    assert agents[0].finisher_name


def test_training_improves_attributes() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    agent = TalentPool.load_free_agents(repo_root)[0]
    trainer = TalentTrainer()

    upgraded_finisher = trainer.train_finisher(agent, weeks=4, coach_skill=80)
    upgraded_promo = trainer.train_promo(agent, weeks=3, coach_skill=70)
    upgraded_safety = trainer.train_safety(agent, weeks=5, coach_skill=75)

    assert upgraded_finisher.finisher_popularity > agent.finisher_popularity
    assert upgraded_promo.promo > agent.promo
    assert upgraded_safety.safety > agent.safety
    assert upgraded_safety.injures_others_risk <= agent.injures_others_risk
