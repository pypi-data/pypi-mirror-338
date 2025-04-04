import sys
import os
import json

# Add the project root path (one level up) to the Python search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from openhab import OpenHABClient, Tags

class TagsTest:
    def __init__(self, client: OpenHABClient):
        self.tagsAPI = Tags(client)

    def testGetTags(self, language: str = None):
        """Retrieve all tags"""
        print("\n~~~~ Test #1 getTags() ~~~~\n")

        try:
            allTags = self.tagsAPI.getTags(language)
            print(json.dumps(allTags, indent=4))
        except Exception as e:
            print(f"Error retrieving tags: {e}")

    def testCreateTag(self, tagData: dict, language: str = None):
        """Create a new tag"""
        print("\n~~~~ Test #2 createTag(tagData) ~~~~\n")

        try:
            response = self.tagsAPI.createTag(tagData, language)
            print("Tag created:", json.dumps(response, indent=4))
        except Exception as e:
            print(f"Error creating tag: {e}")

    def testGetTag(self, tagID: str, language: str = None):
        """Retrieve details for a specific tag"""
        print("\n~~~~ Test #3 getTag(tagID) ~~~~\n")

        try:
            tagDetails = self.tagsAPI.getTag(tagID, language)
            print(json.dumps(tagDetails, indent=4))
        except Exception as e:
            print(f"Error retrieving tag {tagID}: {e}")

    def testUpdateTag(self, tagID: str, updatedTagData: dict, language: str = None):
        """Update a tag"""
        print("\n~~~~ Test #4 updateTag(tagID) ~~~~\n")

        try:
            self.tagsAPI.updateTag(tagID, updatedTagData, language)
            print(f"Tag {tagID} updated successfully.")
        except Exception as e:
            print(f"Error updating tag {tagID}: {e}")

    def testDeleteTag(self, tagID: str, language: str = None):
        """Delete a tag"""
        print("\n~~~~ Test #5 deleteTag(tagID) ~~~~\n")

        try:
            self.tagsAPI.deleteTag(tagID, language)
            print(f"Tag {tagID} deleted successfully.")
        except Exception as e:
            print(f"Error deleting tag {tagID}: {e}")
