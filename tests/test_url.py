from app import app


class TestViews:
    # выполняется перед тестом
    def setup(self):
        # создаем тестовый клиент для тестирования
        app.testing = True
        self.client = app.test_client()

    def test_page_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_my_page(self):
        response = self.client.get("/my_page/")
        assert response.status_code == 200

    def test_load_candidate_page(self):
        response = self.client.get("/candidate/1")
        assert response.status_code == 200

    def test_load_candidates_by_name(self):
        response = self.client.get("/search/day/1")
        assert response.status_code == 308

    def test_load_candidates_by_skills(self):
        response = self.client.get("/skill/flask/1")
        assert response.status_code == 308
    def test_candidate_search(self):
        response = self.client.get("/search/?Search=day")
        assert response.status_code == 200


# выполняется после теста
def teardown(self):
    app.testing = False
