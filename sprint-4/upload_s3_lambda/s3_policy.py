# essa política permite que a função Lambda acesse objetos do bucket

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowLambdaAccessToS3Objects",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bktest4/*"  #arn:aws:s3:::{nome_bucket}/*
        }
    ]
}