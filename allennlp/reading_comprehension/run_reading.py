### author: Chen Zheng
### 10/05/2022

from allennlp.predictors.predictor import Predictor
import allennlp_models.rc

##########################################################################################################################
# The model implements a reading comprehension model patterned after the proposed model in 
# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al, 2018), 
# with improvements borrowed from the SQuAD model in the transformers project. 
# It predicts start tokens and end tokens with a linear layer on top of word piece embeddings.
##########################################################################################################################

### wget https://storage.googleapis.com/allennlp-public-models/transformer-qa.2021-02-11.tar.gz
predictor = Predictor.from_path("transformer-qa.2021-02-11.tar.gz")

qa_question = "Who stars in The Matrix?"
qa_passage = 'The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.'
output = predictor.predict(
    passage=qa_passage,
    question= qa_question
)

##########################################################################################################################
## output format
##########################################################################################################################
print(output)

# {
#     'span_start_logits': [-2.442636728286743, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -5.40069580078125, -7.281312465667725, -10.520407676696777, -9.809059143066406, -8.275628089904785, -9.324617385864258, -10.958069801330566, -9.582011222839355, -9.6669340133667, -8.877446174621582, -11.414945602416992, -10.091476440429688, -11.070568084716797, -8.492741584777832, -8.106295585632324, -8.853500366210938, -10.181503295898438, -10.240874290466309, -10.599491119384766, -8.83584976196289, -3.886960983276367, 3.317272901535034, -6.782419681549072, -4.046055793762207, -9.11877727508545, -7.180045127868652, -10.492090225219727, -9.139832496643066, -10.792901039123535, -10.113704681396484, -9.372051239013672, -7.260406017303467, -10.963165283203125, -10.324016571044922, -8.130123138427734, -9.255364418029785, -6.9815754890441895, -10.129695892333984, -9.176948547363281, -9.928766250610352, -10.248723030090332, -8.764613151550293, -9.693769454956055, -10.084589958190918, -7.653212070465088, -5.473386287689209, -3.4028234663852886e+38], 
#     'span_end_logits': [-1.672015905380249, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38, -8.167206764221191, -3.700436592102051, -7.848005294799805, -9.9476957321167, -8.431559562683105, -10.04885482788086, -8.7389497756958, -8.974319458007812, -8.634963989257812, -8.802312850952148, -9.310943603515625, -9.086554527282715, -10.169046401977539, -8.744050025939941, -8.464509963989258, -7.5854692459106445, -9.2030611038208, -9.53093147277832, -6.622220993041992, -6.895380973815918, -7.097151279449463, -5.701584815979004, -6.346024513244629, 0.43006908893585205, -4.301146507263184, -7.420931816101074, -6.921352386474609, -7.982322692871094, -6.790467739105225, -3.2069971561431885, -4.050369739532471, -6.543085098266602, -7.243873596191406, -7.626040935516357, -2.121096611022949, -3.849494457244873, -5.533522129058838, -6.681992530822754, -1.4695918560028076, -2.302046537399292, -5.481761932373047, -4.453017711639404, -3.736841917037964, -5.715268135070801, 3.477113962173462, 1.4098365306854248, -3.4028234663852886e+38], 
#     'best_span_scores': 6.794386863708496, 
#     'best_span_str': 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano', 
#     'best_span': [21, 44], 
#     'id': '1', 
#     'context_tokens': ['The', 'ĠMatrix', 'Ġis', 'Ġa', 'Ġ1999', 'Ġscience', 'Ġfiction', 'Ġaction', 'Ġfilm', 'Ġwritten', 'Ġand', 'Ġdirected', 'Ġby', 'ĠThe', 'ĠW', 'ach', 'ows', 'k', 'is', ',', 'Ġstarring', 'ĠKe', 'anu', 'ĠReeves', ',', 'ĠLaure', 'nce', 'ĠFish', 'burn', 'e', ',', 'ĠCarrie', '-', 'Anne', 'ĠMoss', ',', 'ĠHugo', 'ĠWe', 'aving', ',', 'Ġand', 'ĠJoe', 'ĠPant', 'ol', 'iano', '.']
# }









