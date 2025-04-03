from typing import List, Dict, Tuple


class ConversationMemory:
    """
    Stores conversation history on a per-agent basis.
    Key: agent_id (int)
    Value: list of messages (List[Dict])

    Each message is a dictionary of the form:
        {"agent_id": <some int>, "content": <str>, ...}

    We keep only the most recent `k_recent * 3` messages per agent
    to avoid excessive memory usage.
    """

    def __init__(self, k_recent: int = 4):
        """
        :param k_recent: Number of "recent" conversation chunks to keep.
                         In practice, we store 3 messages for each "chunk,"
                         so this effectively keeps the last k_recent * 3 messages.
        """
        self._conversations: Dict[int, List[Dict]] = {}
        self.k_recent = k_recent*3 # One conversation takes up three message: topic, first response, final response

    def record_conversation(self, agent_pair: Tuple[int, int], messages: List[Dict]):
        """
        Appends a list of messages to both agents' conversation histories.
        Only keeps the most recent k_recent * 3 messages for each agent.

        :param agent_pair: A tuple of (agent1_id, agent2_id).
        :param messages: A list of message dicts to record.
        """
        agent1_id, agent2_id = agent_pair

        # Ensure both agents have an entry in the conversations dict
        if agent1_id not in self._conversations:
            self._conversations[agent1_id] = []
        if agent2_id not in self._conversations:
            self._conversations[agent2_id] = []

        # Append messages to agent1's conversation
        self._conversations[agent1_id].extend(messages)
        # Truncate to the most recent k_recent
        self._conversations[agent1_id] = self._conversations[agent1_id][-self.k_recent:]

        # Append messages to agent2's conversation
        self._conversations[agent2_id].extend(messages)
        # Truncate to the most recent k_recent
        self._conversations[agent2_id] = self._conversations[agent2_id][-self.k_recent:]

    def fetch_conversation(self, agent_id: int) -> List[Dict]:
        """
        Returns the list of messages for a single agent's entire conversation history.
        If there's no prior conversation for this agent, return an empty list.

        :param agent_id: The agent whose conversation we want to retrieve.
        :return: The agent's list of messages.
        """
        return self._conversations.get(agent_id, [])

    def clear_conversation(self, agent_id: int):
        """
        Remove all messages for the given agent.

        :param agent_id: The agent whose conversation should be cleared.
        """
        if agent_id in self._conversations:
            del self._conversations[agent_id]


class ConversationMemory2:
    """
    A typical conversation is a list of messages, where each message looks like:
                   {"agent_id"<some int>: content, ...}
    """

    def __init__(self):
        # Stores conversation history for each pair of agents.
        # Key: (agent_id1, agent_id2) - stored in sorted form so (3,5) == (5,3).
        # Value: list of messages.
        self._conversations = {}

    def _get_key(self, agent1_id, agent2_id):
        """
        Return a canonical (sorted) tuple so that order doesn't matter.
        """
        return tuple(sorted((agent1_id, agent2_id)))

    def record_conversation(self, agent_pair: Tuple, messages: List[Dict]):
        """
        Append a list of messages to the existing conversation history for these agents.
        If no conversation exists yet, initialize a new history.
        """
        agent1_id, agent2_id = agent_pair
        key = self._get_key(agent1_id, agent2_id)
        if key not in self._conversations:
            self._conversations[key] = []
        self._conversations[key].extend(messages)
        # Keep only the most recent 8 conversations between them
        self._conversations[key] = self._conversations[key][-8:]


    def fetch_conversation(self, agent_pair):
        """
        Return the list of messages for the conversation between these agents.
        If there's no prior conversation, return an empty list.
        """
        agent1_id, agent2_id = agent_pair
        key = self._get_key(agent1_id, agent2_id)
        return self._conversations.get(key, [])

    def clear_conversation(self, agent1_id, agent2_id):
        """
        Remove all messages for the conversation between these agents.
        """
        key = self._get_key(agent1_id, agent2_id)
        if key in self._conversations:
            del self._conversations[key]



if __name__ == '__main__':
    # memory = ConversationMemory2()

    memory = ConversationMemory(k_recent=8)

    # Example usage:
    messages_batch = [
        {"agent_id": 1, "content": "Hi there!"},
        {"agent_id": 2, "content": "Hello! How are you?"},
        {"agent_id": 1, "content": "I'm good, thanks!"}
    ]

    # Record conversation between agent 1 and agent 2
    memory.record_conversation((1, 2), messages_batch)

    # Fetch conversation for agent 1
    convo_agent1 = memory.fetch_conversation(1)
    print("Agent 1 Conversation:", convo_agent1)

    # Fetch conversation for agent 2
    convo_agent2 = memory.fetch_conversation(2)
    print("Agent 2 Conversation:", convo_agent2)

    # Clear conversation for agent 1
    memory.clear_conversation(1)
    print("Agent 1 Conversation After Clearing:", memory.fetch_conversation(1))


