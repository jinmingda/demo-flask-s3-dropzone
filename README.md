This is a Flask app that demonstrates how to upload file(s) directly to S3 using **pre-signed post**.
The frontend is powered by Dropzone.js that enables features like drag-and-drop, queued upload, etc.

## Prerequisite

Make sure server has sufficient IAM permissions to generate S3 pre-signed post.
Please check the following links to know more about IAM permissions.

* ![https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html)

## Example

### Success
![success](./success.gif)

### Error
![error](./error.gif)

## Reference

* [https://www.dropzonejs.com/](https://www.dropzonejs.com/)
* [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html#generating-presigned-posts)
