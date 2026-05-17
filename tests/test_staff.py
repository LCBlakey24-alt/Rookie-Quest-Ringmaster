from ringmaster.staff import RosterNeed, StaffMember, StaffOffice


def test_staff_synergy_balances_bonus_and_penalties() -> None:
    office = StaffOffice()
    staff = [
        StaffMember("w1", "Mira Quill", "writer", "sports_drama", 82, 45000),
        StaffMember("t1", "Dex Volt", "technical", "sports_drama", 78, 42000),
        StaffMember("m1", "Echo Rune", "music", "cinematic", 88, 50000),
    ]
    need = RosterNeed(style_focus="sports_drama", technical_demand=22, creative_demand=26)
    report = office.evaluate_synergy(staff, need, budget=120000)

    assert report.creative_bonus > 0
    assert report.technical_bonus > 0
    assert report.mismatch_penalty > 0  # cinematic music hire mismatches core style


def test_payroll_pressure_when_over_budget() -> None:
    office = StaffOffice()
    staff = [StaffMember("x", "High Cost", "writer", "sports_drama", 90, 250000)]
    need = RosterNeed(style_focus="sports_drama", technical_demand=10, creative_demand=10)
    report = office.evaluate_synergy(staff, need, budget=100000)
    assert report.payroll_pressure > 0
