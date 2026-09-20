"""
나만의 프롬프트 관리 프로그램
"""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 작성한 프롬프트를 기본 데이터로 등록합니다."""
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": (
                "당신은 10년 경력의 전문 블로거입니다. "
                "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. "
                "서론, 본론, 결론 구조를 갖추고, "
                "독자의 관심을 끄는 제목을 3개 제안해주세요."
            ),
            "category": "텍스트 생성",
            "favorite": True,
        },
        {
            "title": "제품 썸네일 생성",
            "content": (
                "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. "
                "배경은 화이트 톤으로 하고, 제품이 정중앙에 위치하도록 구성해주세요."
            ),
            "category": "이미지 생성",
            "favorite": False,
        },
        {
            "title": "IT 컨설턴트 페르소나",
            "content": (
                "당신은 15년 경력의 IT 컨설턴트입니다. "
                "고객사의 디지털 전환 전략을 수립하고, "
                "각 부서별로 실행 가능한 로드맵을 제시해주세요."
            ),
            "category": "페르소나",
            "favorite": False,
        },
    ]


def show_menu():
    """메인 메뉴를 화면에 출력합니다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def get_non_empty_input(prompt_message):
    """빈 값이 입력되면 다시 입력을 요청합니다."""
    while True:
        value = input(prompt_message).strip()
        if value:
            return value
        print("입력값이 비어있습니다. 다시 입력해주세요.")


def select_category():
    """미리 정의된 카테고리 중 선택하거나 직접 입력합니다."""
    print("\n카테고리 선택:")
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {category}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    choice = input("선택: ").strip()
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(CATEGORIES):
            return CATEGORIES[choice_num - 1]
        if choice_num == len(CATEGORIES) + 1:
            return get_non_empty_input("카테고리 이름 입력: ")

    print("잘못된 입력입니다. '기타'로 등록합니다.")
    return "기타"


def add_prompt(prompts):
    """새로운 프롬프트를 등록합니다."""
    print("\n=== 프롬프트 추가 ===")
    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")
    category = select_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


def main():
    prompts = get_default_prompts()

    # 아직 메뉴 선택 분기(if/elif)는 만들지 않고,
    # add_prompt()가 잘 동작하는지 확인하기 위한 임시 호출입니다.
    show_menu()
    add_prompt(prompts)
    print(f"\n현재 등록된 프롬프트 수: {len(prompts)}개")


if __name__ == "__main__":
    main()