import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from patee import MonolingualSingleFilePair, MultilingualSingleFile, MonolingualSingleFile


@dataclass(frozen=True)
class StepContext:
    step_dir: Union[Path, None]


@dataclass(frozen=True)
class DocumentSource:
    document_path: Path
    iso2_language: str

    @staticmethod
    def from_monolingual_file(file: MonolingualSingleFile) -> 'DocumentSource':
        return DocumentSource(file.document_path, file.iso2_language)

    @staticmethod
    def from_multilingual_file(file: MultilingualSingleFile, language_idx: int) -> 'DocumentSource':
        return DocumentSource(file.document_path, file.iso2_languages[language_idx])


@dataclass(frozen=True)
class DocumentContext:
    source: DocumentSource
    text: str
    extra: dict

    def dump_to(self, result_dir: Path):
        file_path = result_dir / f"{self.source.document_path.stem}.txt"
        file_path.write_text(self.text)

        if len(self.extra) > 0:
            extra_path = result_dir / f"{self.source.document_path.stem}_extra.json"
            extra_path.write_text(json.dumps(self.extra, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def load_from(original_context: "DocumentContext", current_dir: Path) -> "DocumentContext":
        if not current_dir.is_dir():
            raise ValueError(f"out_dit path {current_dir} is not a directory")

        text = (current_dir / f"{original_context.source.document_path.stem}.txt").read_text()
        extra = {}

        return DocumentContext(original_context.source, text, extra)


@dataclass(frozen=True)
class DocumentPairContext:
    document_1: DocumentContext
    document_2: DocumentContext

    def dump_to(self, out_dir: Path) -> None:
        if not out_dir.is_dir():
            raise ValueError(f"out_dit path {out_dir} is not a directory")

        self.document_1.dump_to(out_dir)
        self.document_2.dump_to(out_dir)

    @staticmethod
    def read_from(original_context: "DocumentPairContext", current_dir: Path) -> "DocumentPairContext":
        if not current_dir.is_dir():
            raise ValueError(f"out_dit path {current_dir} is not a directory")

        document_1 = DocumentContext.load_from(original_context.document_1, current_dir)
        document_2 = DocumentContext.load_from(original_context.document_2, current_dir)

        return DocumentPairContext(document_1, document_2)


@dataclass(frozen=True)
class StepResult:
    context: Union[DocumentPairContext, None]
    should_stop_pipeline: bool = False
    skipped: bool = False

    def __post_init__(self):
        if self.should_stop_pipeline == True and self.context is not None:
            raise ValueError("Cannot stop pipeline and have a context at the same time.")
        if self.should_stop_pipeline == False and self.context is None:
            raise ValueError("Cannot have a context and not stop pipeline at the same time.")


class Step(ABC):
    """Base class for all extraction steps."""

    def __init__(self, name: str):
        """Initialize the step."""
        self.name = name


class ParallelExtractStep(Step):
    """Base class for all extraction steps."""

    def __init__(self, name: str):
        super().__init__(name)

    @abstractmethod
    def extract(self, context: StepContext,
                source: Union[MonolingualSingleFilePair, MultilingualSingleFile]) -> StepResult:
        pass


class ParallelProcessStep(Step):
    """Base class for all processing steps."""

    def __init__(self, name: str):
        super().__init__(name)

    @abstractmethod
    def process(self, context: StepContext,
                source: DocumentPairContext) -> StepResult:
        pass



