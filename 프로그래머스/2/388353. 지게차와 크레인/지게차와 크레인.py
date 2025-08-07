from collections import defaultdict, deque


def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    # 1. 초기화
    # storage를 수정 가능한 리스트의 리스트로 변환
    grid = [list(row) for row in storage]

    # 아이템 종류별 위치 저장 (조회를 빠르게 하기 위함)
    item_locations = defaultdict(set)
    for r in range(n):
        for c in range(m):
            item_locations[grid[r][c]].add((r, c))

    # 남은 컨테이너 수
    remaining_items = n * m

    # '접근 가능한 빈 공간'을 추적하는 배열
    accessible_empty = [[False] * m for _ in range(n)]

    # 방향 벡터 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def forklift(y, x):

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if accessible_empty[ny][nx]:
                    return True
            else:
                return True
        return False

    # 2. 메인 로직: 요청 처리 루프
    for req in requests:
        item_type = req[0]

        # 처리해야 할 좌표들 (set을 list로 변환하여 순회 중 변경에 영향 없도록 함)
        coords_to_process = list(item_locations[item_type])

        # 새로 접근 가능해진 빈 공간들을 담을 큐
        newly_accessible_q = deque()

        # 제거된 컨테이너 좌표
        removed_coords = set()

        if len(req) == 1:  # 지게차(Forklift) 요청
            for r, c in coords_to_process:
                is_accessible = forklift(r, c)

                if is_accessible:
                    removed_coords.add((r, c))
                    grid[r][c] = '-'
                    newly_accessible_q.append((r, c))  # 새로 생긴 빈 공간은 이제 접근 가능

        else:  # 크레인(Crane) 요청
            for r, c in coords_to_process:
                removed_coords.add((r, c))
                grid[r][c] = '-'

                # 새로 생긴 빈 공간이 경계에 있거나, 기존의 '접근 가능한 빈 공간'과 인접하면 큐에 추가
                is_seed =  forklift(r, c)
                if is_seed:
                    newly_accessible_q.append((r, c))

        # 3. 상태 업데이트
        if removed_coords:
            remaining_items -= len(removed_coords)
            item_locations[item_type] -= removed_coords

        # 4. '접근 가능한 빈 공간' 전파 (BFS)
        # 새로 생긴 '접근 가능한 빈 공간'들로부터 탐색을 시작하여, 
        # 이로 인해 연결되는 다른 모든 빈 공간들의 상태를 업데이트
        while newly_accessible_q:
            r, c = newly_accessible_q.popleft()

            if accessible_empty[r][c]:
                continue

            accessible_empty[r][c] = True

            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if 0 <= nr < n and 0 <= nc < m and not accessible_empty[nr][nc] and grid[nr][nc] == '-':
                    newly_accessible_q.append((nr, nc))

    return remaining_items