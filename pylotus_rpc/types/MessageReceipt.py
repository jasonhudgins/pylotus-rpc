from dataclasses import dataclass
from typing import Any

@dataclass
class MessageReceipt:
    """
    Represents a receipt for a Filecoin message.
    
    Attributes:
    - ExitCode: The exit code after the message was processed.
    - Return: Any return value from the message execution.
    - GasUsed: The amount of gas used to process the message.
    """
    
    ExitCode: int
    Return: Any
    GasUsed: int
