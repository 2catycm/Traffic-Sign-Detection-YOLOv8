import wandb
import wandb_train
def sweep():
    wandb.init()
    # Get hyp dict from sweep agent. Copy because train() modifies parameters which confused wandb.
    # params = vars(wandb.config).get("_items").copy()
    wandb_train.main(wandb.config)

if __name__ == "__main__":
    sweep()
