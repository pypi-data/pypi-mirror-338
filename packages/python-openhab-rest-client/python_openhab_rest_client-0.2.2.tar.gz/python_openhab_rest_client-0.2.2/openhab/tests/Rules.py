import sys
import os
import json

# Add the project root path (one level up) to the Python search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from openhab import OpenHABClient, Rules

class RulesTest:
    def __init__(self, client: OpenHABClient):
        self.rulesAPI = Rules(client)

    def testGetRules(self, prefix=None, tags=None, summary=False, staticDataOnly=False):
        """ Retrieve all rules """
        print("\n~~~~ Test #1 getRules() ~~~~\n")

        try:
            rules = self.rulesAPI.getRules(prefix, tags, summary, staticDataOnly)
            print(json.dumps(rules, indent=4))
        except Exception as e:
            print(f"Error retrieving rules: {e}")

    def testGetRule(self, ruleID: str):
        """ Retrieve details of a specific rule """
        print("\n~~~~ Test #2 getRule(ruleID) ~~~~\n")

        try:
            rule = self.rulesAPI.getRule(ruleID)
            print(json.dumps(rule, indent=4))
        except Exception as e:
            print(f"Error retrieving rule {ruleID}: {e}")

    def testCreateRule(self, ruleData: dict):
        """ Create a new rule """
        print("\n~~~~ Test #3 createRule(ruleData) ~~~~\n")

        try:
            self.rulesAPI.createRule(ruleData)
            print("New Rule created successfully.")
        except Exception as e:
            print(f"Error creating rule: {e}")

    def testUpdateRule(self, ruleID: str, ruleData: dict):
        """ Update an existing rule """
        print("\n~~~~ Test #4 updateRule(ruleID, ruleData) ~~~~\n")

        try:
            self.rulesAPI.updateRule(ruleID, ruleData)
            print("Rule updated successfully.")
        except Exception as e:
            print(f"Error updating rule {ruleID}: {e}")

    def testSetRuleState(self, ruleID: str, state: bool):
        """ Enable or disable a rule """
        action = "enabled" if state else "disabled"
        print("\n~~~~ Test #5 setRuleState(ruleID, state) ~~~~\n")

        try:
            self.rulesAPI.setRuleState(ruleID, state)
            print(f"Rule {ruleID} {action}.")
        except Exception as e:
            print(f"Error setting rule state for {ruleID}: {e}")

    def testDeleteRule(self, ruleID: str):
        """ Delete a rule """
        print("\n~~~~ Test #6 deleteRule(ruleID) ~~~~\n")

        try:
            self.rulesAPI.deleteRule(ruleID)
            print("Rule deleted successfully.")
        except Exception as e:
            print(f"Error deleting rule {ruleID}: {e}")

    def testRunNow(self, ruleID: str, contextData: dict = None):
        """ Execute a rule immediately """
        print("\n~~~~ Test #7 runNow(ruleID) ~~~~\n")

        try:
            self.rulesAPI.runNow(ruleID, contextData)
            print("Rule executed successfully.")
        except Exception as e:
            print(f"Error executing rule {ruleID}: {e}")
