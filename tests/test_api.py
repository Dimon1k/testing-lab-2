def test_api_endpoint(global_config):
	assert global_config["base_url"] == "https://api.test.com"
