# -*- coding: utf-8 -*-
execfile("core.py")
arm_rates = [0.012, 0.013, 0.013, 0.012, 0.012, 0.012, 0.011, 0.011, 0.011, 0.01, 0.01]
arms = [BernoulliArm(r) for r in arm_rates]

# 各armの試行回数
counts = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 各armのClick率
values = [0.012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#探索の割合とarm情報を引数にクラスを設定
algo1 = EpsilonGreedy(0.5, counts, values)

for t in range(10000):
    #armを選択する
    chosen_arm = algo1.select_arm()
    #選択したarmのクリック率によりクリック有無を0,1で返却
    reward = arms[chosen_arm].draw()
    # 選択したarmのクリック率更新する
    algo1.update(chosen_arm, reward)

#選択回数
print(counts)
#試行後の評価確率
print([round(val,4) for val in values])



def calc_ecpm(algo):
    total = sum(algo.counts) - 10000
    ecpm = 0.0
    for idx, count in enumerate(algo.counts):
        if idx == 0:
            count -= 10000
        if count == 0:
            continue
        ecpm += 1000 * 60 * algo.values[idx] * float(count)/total
    return ecpm