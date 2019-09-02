# -*- coding: utf-8 -*-
execfile("core.py")

def calc_ecpm(algo):

    #
    total = sum(algo.counts) - 10000
    ecpm = 0.0
    for idx, count in enumerate(algo.counts):
        if idx == 0:
            count -= 10000
        if count == 0:
            continue
        ecpm += 1000 * 60 * algo.values[idx] * float(count)/total
    return ecpm


def run_eg(ep, counts, values, arms):
    algo = EpsilonGreedy(ep, counts, values)
    for t in xrange(10000):
        chosen_arm = algo.select_arm()
        reward = arms[chosen_arm].draw()
        algo.update(chosen_arm, reward)
    return calc_ecpm(algo)


def run():
    data = []
    arm_rates = [0.012, 0.013, 0.013, 0.012, 0.012, 0.012, 0.011, 0.011, 0.011, 0.01, 0.01]
    arms = [BernoulliArm(r) for r in arm_rates]
    counts = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    values = [0.012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ep in xrange(1, 10):
        print ep * 0.1
        for _ in xrange(10000):
            data.append((ep*0.1, run_eg(ep*0.1, counts, values, arms)))
    return pandas.DataFrame(data, columns=['ep', 'epcm'])

result = run()
result.boxplot(by="ep")