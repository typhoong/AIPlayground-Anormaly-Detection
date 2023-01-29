""" [수치] 전력설비 이상 탐지 모델 - 평가 코드

updated: 211116 (Taehoon Kim)
"""


CLS_DICT = {
    "정상": 0,
    "비정상": 1
}

import sys
import pandas as pd
from sklearn.metrics import f1_score


def load_result(path, pred=False):
    try:
        result = pd.read_csv(path)

        if pred is False: # answer
            p_type_li = result['public'].tolist()
        else: # prediction
            for label in ['label']:
                assert label in result.columns, f'Column ({label}) is missing'
            p_type_li = None

        label = [CLS_DICT[x] for x in list(result['label'])]

        return list(result['ID']), label, p_type_li

    except Exception as e:
        assert False, e


def evaluation_metric(label, prediction):
    return f1_score(label, prediction, average='macro')


def evaluate(label, prediction):
    label = list(map(str, label))
    prediction = list(map(str, prediction))
    return evaluation_metric(label, prediction)


def average_f1score(answer, pred):

    a_id, a_answer, p_type_li = load_result(answer)
    p_id, p_pred, _ = load_result(pred, pred=True)

    assert a_id == p_id, 'Please match the order with the sample submission.'
    assert len(a_id) == len(p_id), 'The number of predictions and answers are not the same'
    assert set(p_id) == set(a_id), 'The prediction ids and answer ids are not the same'

    pub_a_id, pub_answer, prv_a_id, prv_answer = [], [], [], []
    pub_p_id, pub_pred, prv_p_id, prv_pred = [], [], [], []

    for idx, t in enumerate(p_type_li):
        if t:
            pub_a_id.append(a_id[idx])
            pub_answer.append(a_answer[idx])
            pub_p_id.append(p_id[idx])
            pub_pred.append(p_pred[idx])
        else:
            prv_a_id.append(a_id[idx])
            prv_answer.append(a_answer[idx])
            prv_p_id.append(p_id[idx])
            prv_pred.append(p_pred[idx])

    # sort
    pub_ans = pd.DataFrame({'ID': pub_a_id, 'answer': pub_answer}).sort_values('ID', ignore_index=True)
    pub_pred = pd.DataFrame({'ID': pub_p_id, 'answer': pub_pred}).sort_values('ID', ignore_index=True)
    prv_ans = pd.DataFrame({'ID': prv_a_id, 'answer': prv_answer}).sort_values('ID', ignore_index=True)
    prv_pred = pd.DataFrame({'ID': prv_p_id, 'answer': prv_pred}).sort_values('ID', ignore_index=True)

    # f1 scores
    score = evaluate(prediction=pub_pred['answer'], label=pub_ans['answer'])
    pScore = evaluate(prediction=prv_pred['answer'], label=prv_ans['answer'])

    return score, pScore


if __name__ == '__main__':

    answer = sys.argv[1]
    pred = sys.argv[2]

    try:
        import time
        start = time.time()
        score, pScore = average_f1score(answer, pred)
        print(f'score={score},pScore={pScore}')
        print(f'Elapsed Time: {time.time() - start}')

    except Exception as e:
        print(f'evaluation exception error: {e}', file=sys.stderr)
        sys.exit()
