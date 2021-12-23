from mmdet.apis import inference_detector, init_detector, show_result_pyplot

def make_prediction(img_path):
    img = mmcv.imread(img_path)
    model.cfg = cfg
    result = inference_detector(model, img)
    show_result_pyplot(model, img, result, score_thr=0.5)
