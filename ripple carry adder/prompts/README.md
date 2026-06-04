# Prompts

SystemVerilog (`.sv`) files for **10 LLM prompt strategies** used to generate a 4-bit ripple carry adder.

Each file contains:

1. The **prompt** (header comments)
2. **RTL** (`full_adder`, `ripple_carry_adder_4bit`, or variant top)
3. A **testbench**

| File | Strategy |
|------|----------|
| `01_zero_shot.sv` | Zero-shot |
| `02_few_shot.sv` | Few-shot |
| `03_chain_of_thought.sv` | Chain of thought |
| `04_role_prompting.sv` | Role prompting |
| `05_instruction_format.sv` | Instruction + format |
| `06_negative_prompting.sv` | Negative prompting |
| `07_constraints_first.sv` | Constraints first (PPA) |
| `08_self_planning.sv` | Self planning |
| `09_iterative_correction.sv` | Iterative correction |
| `10_hybrid.sv` | Hybrid |

Simulate one file at a time:

```bash
iverilog -g2012 -o sim "ripple carry adder/prompts/01_zero_shot.sv"
vvp sim
```
