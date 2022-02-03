## Generic Algorithm 유전 알고리즘

<strong>유전알고리즘은</strong> 자연세계의 진화과정에 기초한 계산모델로 최적화 문제를 해결하는 기법이다. 생물의 진화를 모방한 진화연산의 대표적인 기법으로 실제 진화의 많은 부분을 채용하였고 변이, 교배 연산 등이 존재한다.

![example](https://t1.daumcdn.net/cfile/tistory/263E2C4357334F6217)

### Example Code

```python
import random


def foo(x, y, z):
    return 6*x**3+9*y**2+90*z-25


def fitness(x, y, z):
    ans = foo(x, y, z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)


solutions = []

for s in range(1000):
    solutions.append((random.uniform(0, 10000), random.uniform(
        0, 10000), random.uniform(0, 10000)))

for i in range(10000):
    rankedsolutions = []

    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f'=== Get {i} best solutions')

    print(rankedsolutions[0])

    bestsolutions = rankedsolutions[:100]

    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.9, 1.1)
        e2 = random.choice(elements) * random.uniform(0.9, 1.1)
        e3 = random.choice(elements) * random.uniform(0.9, 1.1)

        newGen.append((e1, e2, e3))

    solutions = newGen

```

## Reinforcement Learning

<strong>Reinforcement Learning</strong>은 <strong>시도와 실패</strong>(Trial and Error)를 통해 학습하는 autonomous, self-teaching system이다. 이것은 보상의 극대화에 초점을 두고 행동하며, 최상의 결과를 얻기 위해 학습한다.

### Snake Game

[1, 0, 0] -> Straight

[0, 1, 0] -> Right

[0, 0, 1] -> Left

<strong>State</strong>

- danger straight
- danger right
- danger left
- direction left
- direction right
- direction up
- direction down
- food left
- food right
- food up
- food down
