# Documentaçāo

Microserviço que presta conta pela transformaçāo dos videos para outras resoluções (1280x720, 640x480) 

## Mapeamento do processo do recebimento do arquivo

- Foi criado um topic e uma subscription do PUBSUB e configurado para receber notificações do BUCKET do cloud storage quando o objecto for subido.
[DOCUMENTAÇĀO GOOGLE](https://cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/add-iam-policy-binding?hl=es_419)
- O microserviço fica lendo a subcription para receber o video. Para conseguir se comunicar com o PUBSUB o microserviço precisou de ser configurado as credenciais GOOGLE_APPLICATION_CREDENTIALS dentro do container [DOCUMENTAÇĀO DEPLOY NO GCE](https://github.com/google-github-actions/setup-gcloud/tree/master/example-workflows/gce)
- O microserviço sabe para qual subscription vai se suscribir porque é configurada a variável SUBSCRIPTION_ID no ENV do GCE.

## Descriçāo das variáveis do arquivo .YAML do Deploy


- **GCE_PROJECT** id do projecto na GCP
- **GCE_INSTANCE** id do GCE gerado quando se cria a instancia.
- **GCE_INSTANCE_ZONE** zona ao qual pertence a instancia criada.
- **GCE_SA_KEY** é o valor do JSON da conta de serviço

OBS: Cada uma dessas variáveis é para que sejam salva no secret da github.