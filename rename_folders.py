import os
import subprocess

mapping = {
    "Zero Shot": "01_Zero_Shot",
    "Few Shot": "02_Few_Shot",
    "Chain of Thought": "03_Chain_of_Thought",
    "Role Prompting": "04_Role_Prompting",
    "Instruction Format": "05_Instruction_Format",
    "Negative Prompting": "06_Negative_Prompting",
    "Constraints First": "07_Constraints_First",
    "Self Planning": "08_Self_Planning",
    "Iterative Correction": "09_Iterative_Correction",
    "Hybrid": "10_Hybrid"
}

base = os.path.join("Booth Multiplier", "GPT-5.5")

for arch in ["Behavioural", "Structural", "Dataflow"]:
    arch_path = os.path.join(base, arch)
    if os.path.exists(arch_path):
        for folder in os.listdir(arch_path):
            if folder in mapping:
                old_path = os.path.join(arch_path, folder)
                new_path = os.path.join(arch_path, mapping[folder])
                print(f"Renaming {old_path} to {new_path}")
                subprocess.run(["git", "mv", old_path, new_path], check=True)
