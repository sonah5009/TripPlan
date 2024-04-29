from math import radians, sin, cos, sqrt, atan2


def calculate_distance(lat1, lon1, lat2, lon2):
    # 지구의 반지름 (단위: km)
    R = 6371.0

    # 위도 및 경도를 라디안으로 변환
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine 공식 적용
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


# 예시: 두 관광지 간의 거리 계산
distance = calculate_distance(36.854016, 127.624184, 37.460459, 127.974758)
print("두 관광지 간의 거리:", distance, "km")
