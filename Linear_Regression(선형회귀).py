import tensorflow as tf
tf.enable_eager_execution()
import numpy as np

# hypothesis = W * x + b : 가설

x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

W = tf.Variable(2.9) # Variable : 메로리에 저장하는 변수(값 지정)
b = tf.Variable(0.5)

hypothesis = W * x_data + b

# reduce_mean : 특정 차원을 제거하고 평균을 구하는 함수
# reduce_mean(x) : 변수 x가 가리키는 배열 전체 원소의 평균을 구한다
# reduce_mean(x, 0) : 열 단위로 평균 / reduce_mean(x, 1) : 행 단위로 평균
# square : 제곱을 계산
cost = tf.reduce_mean(tf.square(hypothesis - y_data))


# Gradient descent : 경사하강알고리즘 / minimize cost를 찾기 위한 알고리즘

# Learning_rate initialize
learning_rate = 0.01

# Gradient descent
# with _ as _ : 파일을 열때 사용
# with문 안에 있는 문장들의 변수(W, b) 변화를 tape 이라는 변수에 저장
with tf.GradientTape() as tape:
    hypothesis = W * x_data + b
    cost = cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# gradient : 경사도 값(cost에 대해 변수들의 대한 기울기(미분) 값을 구함)
W_grad, b_grad = tape.gradient(cost, [W, b])

# assign_sub : A -= B
# learning_rate : grad 값을 얼만큼 반영할 것인지(값이 크면 많이 반영)
W.assign_sub(learning_rate * W_grad)
b.assign_sub(learning_rate * b_grad)

# Gradient descent full code

# Data
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# W, b initialize
W = tf.Variable(2.9)
b = tf.Variable(0.5)

# W, b update
for i in range(100):
    # Gradient descent
    with tf.GradientTape() as tape:
        hypothesis = W * x_data + b
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)
    if i % 10 == 0:
      print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))

print()

# predict
print(W * 5 + b)
print(W * 2.5 + b)
