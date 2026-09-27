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


def format_prompt_line(index, prompt):
    """목록에 표시할 한 줄 형식을 만듭니다."""
    star = " ⭐" if prompt["favorite"] else ""
    return f"{index}. [{prompt['category']}] {prompt['title']}{star}"


def show_list(prompts):
    """저장된 모든 프롬프트를 번호와 함께 출력합니다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, prompt in enumerate(prompts, start=1):
        print(format_prompt_line(idx, prompt))
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category(prompts):
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 출력합니다."""
    print("\n=== 카테고리별 조회 ===")
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {category}")

    choice = input("선택: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return

    selected_category = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected_category]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for idx, prompt in enumerate(filtered, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{idx}. {prompt['title']}{star}")
    print(f"\n총 {len(filtered)}개의 프롬프트")

def search_prompt(prompts):
    """제목 또는 내용에 키워드가 포함된 프롬프트를 검색합니다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = get_non_empty_input("검색어: ")

    results = [
        p for p in prompts
        if keyword in p["title"] or keyword in p["content"]
    ]

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for idx, prompt in enumerate(results, start=1):
        print(format_prompt_line(idx, prompt))
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail(prompts):
    """프롬프트 번호를 입력하면 전체 내용을 출력합니다."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)
    choice = input("\n번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]
    star = "⭐" if prompt["favorite"] else "없음"

    print("\n" + "─" * 30)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(prompt["content"])
    print("─" * 30)    

def main():
    prompts = get_default_prompts()

    show_menu()
    show_detail(prompts)  # 상세 보기 기능 테스트


if __name__ == "__main__":
    main()