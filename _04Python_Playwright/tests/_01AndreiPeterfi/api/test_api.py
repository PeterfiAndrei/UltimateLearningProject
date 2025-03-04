from playwright.sync_api import sync_playwright


def test_get_users():
    with sync_playwright() as p:
        requests = p.request.new_context()
        response = requests.get("https://jsonplaceholder.typicode.com/users")

        assert response.status == 200
        data = response.json()
        print(data)
        header = response.headers.get("content-type")
        print(f"\nThe header is: {header}")
        assert len(data) > 0
