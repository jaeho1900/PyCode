import numpy as np

# 0부터 17까지의 정수를 포함하는 1차원 배열을 생성합니다. (총 18개 요소)
array1 = np.arange(18)

# array1을 2x3x3 형태의 3차원 배열로 변환합니다.
# order='F'는 포트란(Fortran) 스타일의 열 우선 순서(column-major order)로 요소를 채웁니다.
# C 스타일(기본값, order='C')은 행 우선 순서입니다.
array2 = array1.reshape(2,3,3, order='F')

# array2를 다시 1차원 배열로 변환(평탄화)합니다.
# 참고: flatten() 메서드는 새로운 1차원 배열을 '반환'합니다.
# 이 코드에서는 반환된 값을 변수에 저장하지 않았기 때문에, 이 줄은 실질적으로 프로그램의 최종 상태에 영향을 주지 않습니다.
array2.flatten()
