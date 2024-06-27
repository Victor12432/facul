# Esse problema tem um pequeno erro no enunciado, ao ler, você pode ser induzido a achar que a matriz poderá ser apenas rotacionada, e depois percebemos que também poderemos inverter-lá.

def rotate_matrix(m):
    lenght = len(m)

    # Rotaciona a matriz
    return [[m[j][i] for j in range(lenght)] for i in range(lenght - 1, -1, -1)]


def invert_matrix(m):
    lenght = len(m)

    new_matrix = []

    for i in range(lenght):
        new_matrix.append([])

    # Inverte a matrix
    for i in range(lenght):
        for j in range(lenght):
            new_matrix[abs(j - (lenght - 1))].append(m[j][i])

    return new_matrix


def calc_confidence(std, scan) -> float:
    confidence = 0
    lenght = len(std)

    for i in range(lenght):
        for j in range(lenght):
            # Adiciona à porcentagem caso a diferença dos pixels for menor ou igual a 100;
            if abs(std[i][j] - scan[i][j]) > 100:
                continue

            confidence += 100 / lenght**2

    return confidence


L = int(input())

while L != 0:
    std_img, scan_img = [], []
    confidence = 0

    for _ in range(L):
        row = list(map(int, input().split()))

        std_img.append(row)

    for _ in range(L):
        row = list(map(int, input().split()))

        scan_img.append(row)

    for _ in range(5):
        scan_img = rotate_matrix(scan_img)

        new_confidence = calc_confidence(std_img, scan_img)
        confidence = max(confidence, new_confidence)

        new_confidence = calc_confidence(std_img, invert_matrix(scan_img))
        confidence = max(confidence, new_confidence)

    print("%.2f" % confidence)

    L = int(input())