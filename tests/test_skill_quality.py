import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "thinking-prompts"


class SkillQualityTest(unittest.TestCase):
    def test_frontmatter_and_entrypoint_size(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---", skill, re.DOTALL)
        self.assertIsNotNone(frontmatter)
        self.assertRegex(frontmatter.group(1), r"(?m)^name: thinking-prompts$")
        description = re.search(
            r"(?m)^description:\s*(.+)$", frontmatter.group(1)
        )
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description.group(1)), 500)
        self.assertLessEqual(len(skill), 4_000)
        self.assertLessEqual(len(skill.splitlines()), 100)

    def test_all_relative_markdown_links_resolve(self) -> None:
        for source in ROOT.rglob("*.md"):
            content = source.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", content):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(source=source, target=target):
                    self.assertTrue((source.parent / target).resolve().exists())

    def test_execution_references_do_not_embed_prompt_templates(self) -> None:
        for name in ("life-designer.md", "talent-miner.md"):
            reference = (ROOT / "references" / name).read_text(encoding="utf-8")
            template = ROOT / "references" / "prompt-templates" / name
            with self.subTest(name=name):
                self.assertTrue(template.is_file())
                self.assertNotIn("```text", reference)
                self.assertIn("```text", template.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
