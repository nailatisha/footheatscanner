def generate_diagnosis(delta_temp: float) -> tuple[str, int]:
    """
    Returns:
        diagnosis (str)
        confidence (int 0–100)
    """

    if delta_temp < 1.5:
        return "Normal thermal pattern", 85

    elif 1.5 <= delta_temp <= 3.0:
        return "Possible Diabetic Peripheral Neuropathy (DPN)", 75

    else:
        return "Possible Peripheral Arterial Disease (PAD)", 80
