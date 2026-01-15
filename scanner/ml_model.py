import numpy as np
from sklearn.linear_model import LogisticRegression

# Model global (simple & fast)
model = LogisticRegression()

# Dummy training data (nanti bisa ganti dataset Excel kamu) (gw belum masukkin lagi)
X_train = np.array([
    [0.3], [0.5], [0.7], [1.2], [1.5], [2.0]
])
y_train = np.array([
    0, 0, 1, 1, 2, 2
])
# 0 = Normal, 1 = DPN, 2 = PAD

model.fit(X_train, y_train)

LABEL_MAP = {
    0: "Normal",
    1: "Diabetic Peripheral Neuropathy",
    2: "Peripheral Arterial Disease"
}

def predict_diagnosis(delta_temp):
    pred = model.predict([[delta_temp]])[0]
    confidence = max(model.predict_proba([[delta_temp]])[0]) * 100
    return LABEL_MAP[pred], round(confidence, 2)
