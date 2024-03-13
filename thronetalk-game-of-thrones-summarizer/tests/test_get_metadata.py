# '''
# Module that tests `scripts/get_metadata.py`. Makes use of `unittest` module.
# Consists of smoke tests, one-shot test and edge tests.
# '''
# import unittest
# from scripts import (
#     get_show_metadata,
#     write_show_metadata,
#     _format_episode_metadata,
#     get_episode_metadata,
#     write_episode_metadata
# )

# class TestGetMetadata(unittest.TestCase):
#     '''Test suite for `scripts/get_metadata.py`'''
#     mock_path = './data/test/show_metadata.json'
#     mock_data = {
#             'title': 'GOT',
#             'episodes': 70,
#         }

#     # Smoke tests
#     # def test_get_show_metadata_smoke(self):
#     #     '''Smoke test to make sure the function runs properly.'''
#     #     get_show_metadata("0944947")
#     # def test_write_show_metadata_smoke(self):
#     #     '''Smoke test to make sure the function runs properly.'''
#     #     write_show_metadata(self.mock_path, self.mock_data)
#     # def test__format_episode_metadata_smoke(self):
#     #     '''Smoke test to make sure the function runs properly.'''
#     #     _format_episode_metadata(self.mock_data)
#     # def test_get_episode_metadata_smoke(self):
#     #     '''Smoke test to make sure the function runs properly.'''
#     #     get_episode_metadata()
#     # def test_write_episode_metadata_smoke(self):
#     #     '''Smoke test to make sure the function runs properly.'''
#     #     write_episode_metadata(self.mock_path, self.mock_data)

#     # Edge Tests
#     def test_edge_invalid_get_show_metadata(self):
#         '''Edge test for get_show_metadata function.'''
#         with self.assertRaises(TypeError):
#             get_show_metadata()
#         with self.assertRaises(TypeError):
#             get_show_metadata(1234567)
#         with self.assertRaises(ValueError):
#             get_show_metadata("123")

#     # def test_edge_invalid_write_show_metadata(self):
#     #     '''Edge test for write_show_metadata function.'''
#     #     # Check values of first parameter
#     #     with self.assertRaises(ValueError):
#     #         write_show_metadata()
#     #     with self.assertRaises(TypeError):
#     #         write_show_metadata(1234567, self.mock_data)
#     #     with self.assertRaises(ValueError):
#     #         write_show_metadata("", self.mock_data)
#     #     with self.assertRaises(ValueError):
#     #         write_show_metadata(".json", self.mock_data)
#     #     # Check values of second parameter
#     #     with self.assertRaises(ValueError):
#     #         write_show_metadata(self.mock_path)
#     #     with self.assertRaises(ValueError):
#     #         write_show_metadata(self.mock_path, {})

#     def test_edge_invalid__format_episode_metadata(self):
#         '''Edge test for _format_episode_metadata function.'''
#         # with self.assertRaises(ValueError):
#         #     _format_episode_metadata()
#         with self.assertRaises(ValueError):
#             _format_episode_metadata({})
#     # def test_edge_invalid_write_episode_metadata(self):
#     #     '''Edge test for write_episode_metadata function.'''
#     #     # Check values of first parameter
#     #     with self.assertRaises(ValueError):
#     #         write_episode_metadata()
#     #     with self.assertRaises(TypeError):
#     #         write_episode_metadata(1234567, self.mock_data)
#     #     with self.assertRaises(ValueError):
#     #         write_episode_metadata("", self.mock_data)
#     #     with self.assertRaises(ValueError):
#     #         write_episode_metadata(".csv", self.mock_data)
#     #     # Check values of second parameter
#     #     with self.assertRaises(ValueError):
#     #         write_episode_metadata(self.mock_path)
#     #     with self.assertRaises(ValueError):
#     #         write_episode_metadata(self.mock_path, {})

# if __name__ == "__main__":
#     unittest.main()
