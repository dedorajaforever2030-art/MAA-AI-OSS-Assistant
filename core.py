import anthropic

class ClaudeReviewer:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)

    def review_pull_request(self, diff_content):
        """
        يستقبل التغييرات في الكود ويرسلها لكلود لتحليلها.
        """
        prompt = f"Please review the following code changes for bugs and security risks:\n\n{diff_content}"
        
        # إعداد الطلب لنموذج كلود
        response = self.client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content

if __name__ == "__main__":
    print("AI-OSS-Assistant Core initialized. Ready to process repositories.")
