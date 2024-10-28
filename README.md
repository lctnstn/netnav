# Meet NetNav

NetNav provides a pre-configured, easy-to-deploy AWS instance that simplifies testing and demonstrating a variety of AWS networking services.

## Deployment Instructions

1. [Download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the NetNav repository.
1. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
1. [Upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) `netnav.py` to the S3 bucket.
1. [Create a CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) with the `netnav.yaml` template.