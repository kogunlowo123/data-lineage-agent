# Data Lineage Agent — staging environment
include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "../../../modules//appops/vectorstore"
}

inputs = {
  environment = "staging"
  agent_name  = "data-lineage-agent"
}
