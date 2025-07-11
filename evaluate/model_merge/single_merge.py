import torch
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

# ==== Config ====
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument("--local_dir", required=True, type=str, help="The path for your saved model")
    parser.add_argument('--experiment_name', type=str, default="qwen_1.5", help='Name of the experiment')
    parser.add_argument('--global_step', type=int, default=186, help='Global step number')
    parser.add_argument("--base_model_name", default="", type=str, help="The path of the base model")
    parser.add_argument("--hf_upload_path", default=None, type=str, help="The path of the huggingface repo to upload")
    
    args = parser.parse_args()

    actor_ckpt_path = f""  # replace with your path
    output_dir = f""  # where to save the merged model

    # ==== Load base model ====
    print("Loading base model...")
    model = AutoModelForCausalLM.from_pretrained(args.base_model_name)

    # ==== Load actor checkpoint ====
    print(f"Loading VERL actor weights from {actor_ckpt_path}...")
    state_dict = torch.load(actor_ckpt_path, map_location="cpu")

    # ==== Merge weights ====
    print("Merging weights into base model...")
    missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=False)
    print("Missing keys:", missing_keys)
    print("Unexpected keys:", unexpected_keys)

    # ==== Save merged model ====
    print(f"Saving merged model to {output_dir}...")
    tokenizer = AutoTokenizer.from_pretrained(args.base_model_name)
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    print("Done! You can now use this model for evaluation.")

    if args.hf_upload_path:
        # Push to hugging face
        from huggingface_hub import HfApi

        api = HfApi(token="")
        api.create_repo(repo_id=f"{args.hf_upload_path}/{args.experiment_name}_step_{args.global_step}", private=False, exist_ok=True)
        api.upload_folder(folder_path=output_dir, repo_id=f"{args.hf_upload_path}/{args.experiment_name}_step_{args.global_step}", repo_type="model")

