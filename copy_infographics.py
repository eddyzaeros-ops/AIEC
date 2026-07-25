import os, shutil

src_dir = r"C:\Users\administartor\.gemini\antigravity\brain\de4f6ead-1339-4f6e-b8cb-26d51d9479e6"
dst_dir = r"c:\Users\administartor\Downloads\AIEC\images"
os.makedirs(dst_dir, exist_ok=True)

img_map = {
    "ai_eval_matrix.jpg": "ai_eval_matrix_1784972071795.jpg",
    "adversarial_attack_defense.jpg": "adversarial_attack_defense_1784972083155.jpg",
    "rag_triad_eval.jpg": "rag_triad_eval_1784972095130.jpg",
    "hmt_trust_calibration.jpg": "hmt_trust_calibration_1784972106729.jpg",
    "sovereign_ai_test_stack.jpg": "sovereign_ai_test_stack_1784972117102.jpg"
}

for dst_name, src_name in img_map.items():
    s_path = os.path.join(src_dir, src_name)
    d_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(s_path):
        shutil.copy(s_path, d_path)
        print(f"Copied {src_name} -> {dst_name}")

