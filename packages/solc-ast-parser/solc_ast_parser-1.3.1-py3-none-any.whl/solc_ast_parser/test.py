import json
from os import listdir
import os

# from solc_ast_parser.enrichment import restore_ast
from solc_ast_parser.enrichment import restore_function_definitions, restore_storages
from solc_ast_parser.models.ast_models import SourceUnit
from solc_ast_parser.models.base_ast_models import NodeType
from solc_ast_parser.utils import (
    compile_contract_with_standart_input,
    update_node_fields,
)
from solc_ast_parser.comments import insert_comments_into_ast
from solc_ast_parser.utils import create_ast_from_source, create_ast_with_standart_input
from solcx.exceptions import SolcError


def create_contract(pseudocode: str) -> str:
    return f"// SPDX-License-Identifier: MIT\npragma solidity ^0.8.28;\ncontract PseudoContract {{\n\n{pseudocode}\n}}"


# ast = create_ast_with_standart_input(vuln_template)
# path = "../../../pycryptor/data/"
# vuln_files = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f)) and not f.startswith("userx-")]
path = "./"
vuln_files = [
    f
    for f in listdir(path)
    if os.path.isfile(os.path.join(path, f)) and f.endswith(".sol")
]
success = 0

# for file in vuln_files:
#     with open(os.path.join(path, file), "r") as f:
vuln_template = create_contract(
    """
// LLM: Token Decimals Handling Issue - Low
function getReturn(IERC20 tokenFrom, IERC20 tokenTo, uint256 inputAmount) public view returns(uint256 outputAmount) {
  unchecked {
    uint256 fromBalance = tokenFrom.balanceOf(address(this));
    uint256 toBalance = tokenTo.balanceOf(address(this));
    // Something

    require(inputAmount <= toBalance, "input amount is too big");
    uint256 x0 = _ONE * fromBalance / (fromBalance + toBalance);
    
    // Something
    uint256 x1 = _ONE * (fromBalance + inputAmount) / (fromBalance + toBalance);
    uint256 x1subx0 = _ONE * inputAmount / (fromBalance + toBalance);         // Something 1
    // Something
    uint256 amountMultiplier = (
      _C1 * x1subx0 +
      _C2 * _powerHelper(x0) -
      _C2 * _powerHelper(x1)
    ) / x1subx0;
    outputAmount = inputAmount * Math.min(amountMultiplier, _ONE) / _ONE;
  }

}
// LLM: Vulnerable line(s): The function doesn't account for differences in decimal places between tokens, which can lead to incorrect calculations
"""
)

try:
    ast = create_ast_with_standart_input(vuln_template)
    # ast = SourceUnit(**ast)
    # update_node_fields(ast, {"node_type": [NodeType.VARIABLE_DECLARATION.value, NodeType.IDENTIFIER.value], "name": "lpToken"}, {"name": "<|random:collateralId|collId|id>"})
    # update_node_fields(ast, {"node_type": [NodeType.FUNCTION_DEFINITION.value, NodeType.IDENTIFIER.value], "name": "addLPToken"}, {"name": "<|random:tokenExists|exists|check>"})
    with open("contract.json", "w+") as f:
        f.write("!!!!")
        f.write(ast.model_dump_json())

    # new_ast = restore_ast(ast)
    # new_ast = ast


    with open("contract_with_comments.json", "w+") as f:
        f.write(ast.model_dump_json())

    # update_node_fields(
    #     ast,
    #     {
    #         "node_type": [
    #             NodeType.FUNCTION_DEFINITION.value,
    #             NodeType.IDENTIFIER.value,
    #         ],
    #         "name": "_powerHelper",
    #     },
    #     {"name": "<|random:powerHelper|helper|power>"},
    # )
    # vuln_template = vuln_template.replace("_powerHelper", "<|random:powerHelper|helper|power>")

    # update_node_fields(
    #     ast,
    #     {
    #         "node_type": [
    #             NodeType.VARIABLE_DECLARATION.value,
    #             NodeType.IDENTIFIER.value,
    #         ],
    #         "name": "inputAmount",
    #     },
    #     {"name": "<|random:amount|amt|input>"},
    # )

    ast = insert_comments_into_ast(vuln_template, ast)

    for node in ast.nodes:
        if node.node_type == NodeType.CONTRACT_DEFINITION:
            res = "".join([node.to_solidity() for node in node.nodes])

    with open("new_contract.sol", "w+") as f:
      f.write(res)

    # with open("new_contract.json", "w+") as f:
    #     f.write(json.dumps(res.model_dump(), indent=4))

    # res = insert_comments_into_ast(vuln_template, res)
    print([f.name for f in restore_function_definitions(ast)])
    # new_ast = restore_storages(new_ast)
    code = res.to_solidity()


except Exception as e:
    with open("error.txt", "w+") as f:
        f.write(str(e))
    raise e
with open("new_contract.sol", "w+") as f:
    f.write(code)


ast = create_ast_from_source(code)
# parse_ast_to_solidity(new_ast)
success += 1
# print(f"Success: {success}/{len(vuln_files)}")

# VALIDATOR INFO + TIME + STATUS
