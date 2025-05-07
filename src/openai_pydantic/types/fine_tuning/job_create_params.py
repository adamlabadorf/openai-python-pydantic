# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union,List
from typing_extensions import Literal

from ..shared_params.metadata import Metadata

__all__ = [
    "JobCreateParams",
    "Hyperparameters",
    "Integration",
    "IntegrationWandb",
    "Method",
    "MethodDpo",
    "MethodDpoHyperparameters",
    "MethodSupervised",
    "MethodSupervisedHyperparameters",
]


class JobCreateParams(BaseModel):
    model: "Union[str, Literal['babbage-002', 'davinci-002', 'gpt-3.5-turbo', 'gpt-4o-mini']]"
    
    """The name of the model to fine-tune.

    You can select one of the
    [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).
    """

    training_file: "str"
    
    """The ID of an uploaded file that contains training data.

    See [upload file](https://platform.openai.com/docs/api-reference/files/create)
    for how to upload a file.

    Your dataset must be formatted as a JSONL file. Additionally, you must upload
    your file with the purpose `fine-tune`.

    The contents of the file should differ depending on if the model uses the
    [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input),
    [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input)
    format, or if the fine-tuning method uses the
    [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input)
    format.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning)
    for more details.
    """

    hyperparameters: "Optional[Hyperparameters]"= None
    
    """
    The hyperparameters used for the fine-tuning job. This value is now deprecated
    in favor of `method`, and should be passed in under the `method` parameter.
    """

    integrations: "Optional[List[Integration]]"=Field(default_factory=list)
    
    """A list of integrations to enable for your fine-tuning job."""

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    method: "Optional[Method]"= None
    
    """The method used for fine-tuning."""

    seed: "Optional[int]"= None
    
    """The seed controls the reproducibility of the job.

    Passing in the same seed and job parameters should produce the same results, but
    may differ in rare cases. If a seed is not specified, one will be generated for
    you.
    """

    suffix: "Optional[str]"= None
    
    """
    A string of up to 64 characters that will be added to your fine-tuned model
    name.

    For example, a `suffix` of "custom-model-name" would produce a model name like
    `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.
    """

    validation_file: "Optional[str]"= None
    
    """The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation metrics
    periodically during fine-tuning. These metrics can be viewed in the fine-tuning
    results file. The same data should not be present in both train and validation
    files.

    Your dataset must be formatted as a JSONL file. You must upload your file with
    the purpose `fine-tune`.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning)
    for more details.
    """


class Hyperparameters(BaseModel):
    batch_size: "Optional[Union[Literal['auto'], int]]"= None
    
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: "Optional[Union[Literal['auto'], float]]"= None
    
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: "Optional[Union[Literal['auto'], int]]"= None
    
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class IntegrationWandb(BaseModel):
    project: "str"
    
    """The name of the project that the new run will be created under."""

    entity: "Optional[str]"= None
    
    """The entity to use for the run.

    This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered
    WandB API key is used.
    """

    name: "Optional[str]"= None
    
    """A display name to set for the run.

    If not set, we will use the Job ID as the name.
    """

    tags: "Optional[List[str]]"= None
    
    """A list of tags to be attached to the newly created run.

    These tags are passed through directly to WandB. Some default tags are generated
    by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".
    """


class Integration(BaseModel):
    type: "Literal['wandb']"
    
    """The type of integration to enable.

    Currently, only "wandb" (Weights and Biases) is supported.
    """

    wandb: "IntegrationWandb"
    
    """The settings for your integration with Weights and Biases.

    This payload specifies the project that metrics will be sent to. Optionally, you
    can set an explicit display name for your run, add tags to your run, and set a
    default entity (team, username, etc) to be associated with your run.
    """


class MethodDpoHyperparameters(BaseModel):
    batch_size: "Optional[Union[Literal['auto'], int]]"= None
    
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    beta: "Optional[Union[Literal['auto'], float]]"= None
    
    """The beta value for the DPO method.

    A higher beta value will increase the weight of the penalty between the policy
    and reference model.
    """

    learning_rate_multiplier: "Optional[Union[Literal['auto'], float]]"= None
    
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: "Optional[Union[Literal['auto'], int]]"= None
    
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodDpo(BaseModel):
    hyperparameters: "Optional[MethodDpoHyperparameters]"= None
    
    """The hyperparameters used for the fine-tuning job."""


class MethodSupervisedHyperparameters(BaseModel):
    batch_size: "Optional[Union[Literal['auto'], int]]"= None
    
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: "Optional[Union[Literal['auto'], float]]"= None
    
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: "Optional[Union[Literal['auto'], int]]"= None
    
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodSupervised(BaseModel):
    hyperparameters: "Optional[MethodSupervisedHyperparameters]"= None
    
    """The hyperparameters used for the fine-tuning job."""


class Method(BaseModel):
    dpo: "Optional[MethodDpo]"= None
    
    """Configuration for the DPO fine-tuning method."""

    supervised: "Optional[MethodSupervised]"= None
    
    """Configuration for the supervised fine-tuning method."""

    type: "Optional[Literal['supervised', 'dpo']]"= None
    
    """The type of method. Is either `supervised` or `dpo`."""
JobCreateParams.model_rebuild()
Hyperparameters.model_rebuild()
IntegrationWandb.model_rebuild()
Integration.model_rebuild()
MethodDpoHyperparameters.model_rebuild()
MethodDpo.model_rebuild()
MethodSupervisedHyperparameters.model_rebuild()
MethodSupervised.model_rebuild()
Method.model_rebuild()

