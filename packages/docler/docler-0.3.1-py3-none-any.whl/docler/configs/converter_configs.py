"""Converter configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal

from docling.datamodel.pipeline_options import (  # noqa: TC002
    EasyOcrOptions,
    OcrMacOptions,
    RapidOcrOptions,
    TesseractCliOcrOptions,
    TesseractOcrOptions,
)
from pydantic import Field, HttpUrl, SecretStr
from pydantic_settings import SettingsConfigDict

from docler.common_types import DEFAULT_CONVERTER_MODEL, SupportedLanguage
from docler.provider import ProviderConfig
from docler.pydantic_types import ModelIdentifier  # noqa: TC001


if TYPE_CHECKING:
    from docler.converters.base import DocumentConverter


ConverterShorthand = Literal[
    "docling", "marker", "mistral", "llamaparse", "datalab", "azure", "llm"
]

DoclingEngine = Literal[
    "easy_ocr", "tesseract_cli_ocr", "tesseract_ocr", "ocr_mac", "rapid_ocr"
]

UpstageOCRType = Literal["auto", "force"]
UpstageOutputFormat = Literal["markdown", "text", "html"]

AzureModel = Literal[
    "prebuilt-read",
    "prebuilt-layout",
    "prebuilt-idDocument",
    "prebuilt-receipt",
]

AzureFeatureFlag = Literal[
    "ocrHighResolution",
    "languages",
    "barcodes",
    "formulas",
    "keyValuePairs",
    "styleFont",
    "queryFields",
]


LlamaParseMode = Literal[
    "parse_page_without_llm",
    "parse_page_with_llm",
    "parse_page_with_lvm",
    "parse_page_with_agent",
    "parse_document_with_llm",
]


MarkerLLMProvider = Literal["gemini", "ollama", "vertex", "claude"]


def default_languages() -> set[SupportedLanguage]:
    return {"en"}


class BaseConverterConfig(ProviderConfig):
    """Base configuration for document converters."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        raise NotImplementedError


class DoclingConverterConfig(BaseConverterConfig):
    """Configuration for docling-based converter."""

    type: Literal["docling"] = Field("docling", init=False)
    """Type discriminator for docling converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    image_scale: float = Field(default=2.0, gt=0)
    """Scale factor for image resizing."""

    generate_images: bool = True
    """Whether to generate images."""

    ocr_engine: (
        DoclingEngine
        | EasyOcrOptions
        | TesseractCliOcrOptions
        | TesseractOcrOptions
        | OcrMacOptions
        | RapidOcrOptions
    ) = "easy_ocr"
    """OCR engine to use."""

    model_config = SettingsConfigDict(env_prefix="DOCLING_")

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.docling_provider import DoclingConverter

        return DoclingConverter(**self.get_config_fields())


class MarkItDownConfig(BaseConverterConfig):
    """Configuration for MarkItDown-based converter."""

    type: Literal["markitdown"] = Field("markitdown", init=False)
    """Type discriminator for MarkItDown converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.markitdown_provider import MarkItDownConverter

        return MarkItDownConverter(**self.get_config_fields())


class KreuzbergConfig(BaseConverterConfig):
    """Configuration for Kreuzberg document converter.

    Reference:
    https://docs.kreuzberg.ai/configuration
    """

    type: Literal["kreuzberg"] = Field("kreuzberg", init=False)
    """Type identifier for this converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    force_ocr: bool = False
    """Whether to force OCR for all documents."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.kreuzberg_provider import KreuzbergConverter

        return KreuzbergConverter(**self.get_config_fields())


class DataLabConfig(BaseConverterConfig):
    """Configuration for DataLab-based converter."""

    type: Literal["datalab"] = Field("datalab", init=False)
    """Type discriminator for DataLab converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    api_key: SecretStr | None = None
    """DataLab API key. If None, will try env var DATALAB_API_KEY."""

    force_ocr: bool = False
    """Whether to force OCR on every page."""

    use_llm: bool = False
    """Whether to use LLM for enhanced accuracy."""

    max_pages: int | None = Field(default=None, ge=1)
    """Maximum number of pages to process."""

    model_config = SettingsConfigDict(env_prefix="DATALAB_")

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.datalab_provider import DataLabConverter

        return DataLabConverter(**self.get_config_fields())


class LLMConverterConfig(BaseConverterConfig):
    """Configuration for LLM-based converter."""

    type: Literal["llm"] = Field("llm", init=False)
    """Type discriminator for LLM converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    model: ModelIdentifier = DEFAULT_CONVERTER_MODEL
    """LLM model to use."""

    system_prompt: str | None = None
    """Optional system prompt to guide conversion."""

    user_prompt: str | None = None
    """Custom prompt for the conversion task."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.llm_provider import LLMConverter

        return LLMConverter(**self.get_config_fields())


class MistralConfig(BaseConverterConfig):
    """Configuration for Mistral-based converter."""

    type: Literal["mistral"] = Field("mistral", init=False)
    """Type discriminator for Mistral converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    api_key: SecretStr | None = None
    """Mistral API key. If None, will try env var MISTRAL_API_KEY."""

    model_config = SettingsConfigDict(env_prefix="MISTRAL_")

    # right now there only is one model
    # ocr_model: str = "mistral-ocr-latest"
    # """Mistral OCR model to use."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.mistral_provider import MistralConverter

        return MistralConverter(**self.get_config_fields())


class LlamaParseConfig(BaseConverterConfig):
    """Configuration for LlamaParse-based converter."""

    type: Literal["llamaparse"] = Field("llamaparse", init=False)
    """Type discriminator for LlamaParse converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    api_key: SecretStr | None = None
    """LlamaParse API key. Falls back to LLAMAPARSE_API_KEY env var."""

    adaptive_long_table: bool = False
    """Whether to use adaptive long table."""

    parse_mode: LlamaParseMode = "parse_page_with_llm"
    """Parse mode, defaults to "parse_page_with_llm"."""

    model_config = SettingsConfigDict(env_prefix="LLAMAPARSE_")

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.llamaparse_provider import LlamaParseConverter

        return LlamaParseConverter(**self.get_config_fields())


class AzureConfig(BaseConverterConfig):
    """Configuration for Azure Document Intelligence converter."""

    type: Literal["azure"] = Field("azure", init=False)
    """Type discriminator for Azure converter."""

    languages: set[SupportedLanguage] = Field(default_factory=default_languages)
    """List of supported languages for the converter."""

    endpoint: str | None = None
    """Azure endpoint URL. Falls back to AZURE_DOC_INTELLIGENCE_ENDPOINT envvar."""

    api_key: SecretStr | None = None
    """Azure API key. Falls back to AZURE_DOC_INTELLIGENCE_KEY env var."""

    model: AzureModel = "prebuilt-layout"
    """Pre-trained model to use."""

    additional_features: set[AzureFeatureFlag] = Field(default_factory=set)
    """Optional add-on capabilities like BARCODES, FORMULAS, OCR_HIGH_RESOLUTION etc."""

    model_config = SettingsConfigDict(env_prefix="LLAMAPARSE_")

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.azure_provider import AzureConverter

        return AzureConverter(**self.get_config_fields())


class MarkerConfig(BaseConverterConfig):
    """Configuration for Marker-based converter."""

    type: Literal["marker"] = Field("marker", init=False)
    """Type discriminator for Marker converter."""

    dpi: int = Field(default=192, gt=0)
    """DPI setting for image extraction."""

    llm_provider: MarkerLLMProvider | None = None
    """Language model provider to use for OCR."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.marker_provider import MarkerConverter

        return MarkerConverter(**self.get_config_fields())


class UpstageConfig(BaseConverterConfig):
    """Configuration for Upstage Document AI converter."""

    type: Literal["upstage"] = Field("upstage", init=False)
    """Type discriminator for Upstage converter."""

    api_key: SecretStr | None = None
    """Upstage API key. Falls back to UPSTAGE_API_KEY env var."""

    base_url: HttpUrl = HttpUrl("https://api.upstage.ai/v1/document-ai/document-parse")
    """API endpoint URL."""

    # model: str = "document-parse"
    # """Model name for document parsing."""

    ocr: UpstageOCRType = "auto"
    """OCR mode ('auto' or 'force')."""

    output_format: UpstageOutputFormat = "markdown"
    """Output format ('markdown', 'text', or 'html')."""

    base64_categories: list[str] = Field(default_factory=lambda: ["figure", "chart"])
    """Element categories to encode in base64."""

    model_config = SettingsConfigDict(env_prefix="UPSTAGE_")

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.upstage_provider import UpstageConverter

        return UpstageConverter(**self.get_config_fields())


class AggregatedConverterConfig(BaseConverterConfig):
    """Configuration for the aggregated converter."""

    type: Literal["aggregated"] = Field(default="aggregated", init=False)
    """Type discriminator for aggregated converter."""

    converters: list[ConverterConfig] = Field(default_factory=list)
    """List of converter configurations to use."""

    mime_preferences: dict[str, str] = Field(default_factory=dict)
    """Mapping of MIME types or extensions to preferred converter names."""

    def get_provider(self) -> DocumentConverter:
        """Get the converter instance."""
        from docler.converters.aggregated_converter import AggregatedConverter

        return AggregatedConverter.from_config(self)


ConverterConfig = Annotated[
    DataLabConfig
    | DoclingConverterConfig
    | KreuzbergConfig
    | LLMConverterConfig
    | MarkItDownConfig
    | MistralConfig
    | LlamaParseConfig
    | AzureConfig
    | UpstageConfig
    | AggregatedConverterConfig
    | MarkerConfig,
    Field(discriminator="type"),
]
