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


def main():
    prompts = get_default_prompts()
    print(f"현재 등록된 프롬프트 수: {len(prompts)}개")

    # 아직 메뉴 선택 로직은 없고, 메뉴가 출력되는지만 확인하는 임시 코드입니다.
    show_menu()

    # get_non_empty_input()이 잘 동작하는지 확인하는 임시 테스트 코드
    test_value = get_non_empty_input("테스트 입력 (빈 값 입력해보세요): ")
    print(f"입력하신 값: {test_value}")


if __name__ == "__main__":
    main()