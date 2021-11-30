# Documentación

Microservicio encargado de transformar videos para otras resoluciones (1280x720, 640x480)

## Mapa de proceso de como recibe el archivo

- Debe ser creado un topic y una subcription de PUBSUB y debe ser configurado para recibir notificaciones del BUCKET de CLOUD STORAGE cuando el archivo sea subido [DOCUMENTACION GOOGLE](https://cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/add-iam-policy-binding?hl=es_419).

- El microservicio se suscribe a la subcription creada en el paso anterior y recibe los datos del video. Para que el microservicio consiga comunicarse con PUBSUB debe ser configurada la cuenta de servicio GOOGLE_APPLICATION_CREDENTIALS dentro del contrainer [DOCUMENTACION DEPLOY EN Google Compute Engine](https://github.com/google-github-actions/setup-gcloud/tree/master/example-workflows/gce).

- El microservicio sabe para cual subcription se debe suscribir porque es configurado una variable de ambiente llamada SUBSCRIPTION_ID en la instancia creada en Google Compute Engine

## Descripción de las variables del archivo .YAML para Deploy


- **GCE_PROJECT** id del proyecto en GCP
- **GCE_INSTANCE** id de la instancia en Google Compute Engine (se genera al momento de crear la instancia).
- **GCE_INSTANCE_ZONE** zona ao qual pertence a instancia criada.
- **GCE_SA_KEY** El del JSON de la cuenta de servicio.