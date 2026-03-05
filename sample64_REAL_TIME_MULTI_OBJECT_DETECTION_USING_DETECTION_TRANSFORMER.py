import cv2
import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import time

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
PROCESSOR = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
MODEL = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")
MODEL.to(DEVICE)
MODEL.eval()

CAP = cv2.VideoCapture(0)
PREV_TIME = 0
while True:
    RET, FRAME = CAP.read()
    if not RET:
        break
    START = time.time()
    RGB = cv2.cvtColor(FRAME, cv2.COLOR_BGR2RGB)
    IMAGE = Image.fromarray(RGB)
    INPUTS = PROCESSOR(images=IMAGE, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        OUTPUTS = MODEL(**INPUTS)
    TARGET_SIZES = torch.tensor([IMAGE.size[::-1]]).to(DEVICE)
    RESULTS = PROCESSOR.post_process_object_detection(
        OUTPUTS,
        target_sizes=TARGET_SIZES,
        threshold=0.7
    )[0]
    for SCORE, LABEL, BOX in zip(RESULTS["scores"], RESULTS["labels"], RESULTS["boxes"]):
        X1, Y1, X2, Y2 = BOX.int().tolist()
        CLASS_NAME = MODEL.config.id2label[LABEL.item()]
        CONFIDENCE = SCORE.item()
        cv2.rectangle(FRAME, (X1, Y1), (X2, Y2), (0, 255, 0), 2)
        cv2.putText(
            FRAME,
            f"{CLASS_NAME} {CONFIDENCE:.2f}",
            (X1, Y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )
    FPS = 1 / (time.time() - START)
    cv2.putText(FRAME, f"fps: {int(FPS)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("dert", FRAME)
    if cv2.waitKey(1) & 0xFF == 27:
        break

CAP.release()
cv2.destroyAllWindows()
