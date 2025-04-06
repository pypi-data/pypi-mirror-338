#! /usr/bin/env bash

function bluer_ai_publish() {
    local options=$1
    local do_download=$(abcli_option_int "$options" download 1)
    local do_tar=$(abcli_option_int "$options" tar 0)
    local prefix=$(abcli_option "$options" prefix)
    local suffix=$(abcli_option "$options" suffix)

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - $object_name

    bluer_objects_mlflow_tags set $object_name published

    local public_object_name=$(abcli_option "$options" as $object_name)

    if [ "$do_tar" == 1 ]; then
        abcli_log "publishing $object_name -> $public_object_name.tar.gz"

        bluer_objects_upload ~open,solid $object_name
        aws s3 cp \
            $ABCLI_S3_OBJECT_PREFIX/$object_name.tar.gz \
            s3://$ABCLI_AWS_S3_PUBLIC_BUCKET_NAME/$public_object_name.tar.gz
        aws s3 rm \
            $ABCLI_S3_OBJECT_PREFIX/$object_name.tar.gz

        abcli_log "🔗 $ABCLI_PUBLIC_PREFIX/$public_object_name.tar.gz"
        return
    fi

    local object_path=$ABCLI_OBJECT_ROOT/$object_name

    if [[ -z "$prefix$suffix" ]]; then
        abcli_log "publishing $object_name -> $public_object_name"

        aws s3 sync \
            $object_path/ \
            s3://$ABCLI_AWS_S3_PUBLIC_BUCKET_NAME/$public_object_name/

        abcli_log "🔗 $ABCLI_PUBLIC_PREFIX/$public_object_name/"
        return
    fi

    abcli_log "publishing $object_name/$prefix*$suffix -> $public_object_name"

    pushd $object_path >/dev/null
    local filename
    for filename in $(ls *); do
        [[ "$filename" != "$prefix"*"$suffix" ]] && continue

        aws s3 cp \
            $filename \
            s3://$ABCLI_AWS_S3_PUBLIC_BUCKET_NAME/$public_object_name/$filename

        abcli_log "🔗 $ABCLI_PUBLIC_PREFIX/$public_object_name/$filename"
    done
    popd >/dev/null
}
