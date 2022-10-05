### author: Chen Zheng
### 10/03/2022

################################################################################################################################
# Named Entity Recognition is the task of identifying named entities (people, locations, organizations, etc.) in the input text.
################################################################################################################################

from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

### use the command line: wget https://storage.googleapis.com/allennlp-public-models/ner-elmo.2021-02-12.tar.gz
predictor = Predictor.from_path("./ner-elmo.2021-02-12.tar.gz")
output = predictor.predict(
    sentence="AllenNLP is a PyTorch-based natural language processing library developed at the Allen Institute for Artificial Intelligence in Seattle."
)

##########################################################################################################################
## output format
##########################################################################################################################
print(output)

# {'logits': 
#     [
#         [2.868198871612549, -1.033968448638916, -5.2076592445373535, -6.570158004760742, 13.346809387207031, -0.8054488301277161, 1.410940170288086, -0.15849512815475464, -4.46424674987793, -8.539644241333008, -4.480416774749756, -6.735387325286865, -1.02376389503479, -5.678192138671875, -7.190130710601807, -10.081494331359863, -9.93707275390625], 
#         [13.980515480041504, -4.597216606140137, -4.963852882385254, -5.495501518249512, -6.5830841064453125, -4.403265953063965, -4.309296607971191, -1.4541462659835815, -5.8885111808776855, 0.5717153549194336, -4.06989860534668, -2.7064757347106934, -3.4693093299865723, -0.3503861129283905, -0.7222849130630493, -4.643707275390625, -2.75339937210083], 
#         [14.190985679626465, -4.427206993103027, -3.8032655715942383, -7.265738010406494, -7.546986103057861, -3.226066827774048, 1.444269061088562, -6.03985071182251, -6.173473834991455, 0.6189271211624146, -1.834704041481018, -5.9269938468933105, -0.6133951544761658, -4.731712818145752, -1.3994193077087402, -4.398655891418457, -4.331511497497559], 
#         [0.12219241261482239, 0.3360741436481476, -5.630516529083252, -5.380021572113037, 9.67134952545166, 1.8079358339309692, 1.020904541015625, 1.5117822885513306, -3.5099687576293945, -6.370089530944824, -2.536055564880371, -3.460926055908203, -1.0357836484909058, -3.4580869674682617, -5.358729839324951, -9.609668731689453, -7.907097339630127], 
#         [13.602229118347168, -5.493115425109863, -4.474354267120361, -5.603147506713867, -6.051010608673096, -4.248022079467773, -4.073856353759766, -0.7163317203521729, -6.355498313903809, 0.3236733078956604, -4.1917338371276855, -3.180955171585083, -3.6247506141662598, -0.555041491985321, -0.8054872751235962, -4.827136516571045, -3.109463691711426], 
#         [14.010204315185547, -4.53928279876709, -4.168604373931885, -4.817674160003662, -5.865383625030518, -4.961966514587402, -3.1400058269500732, -1.5090086460113525, -6.027421951293945, 0.23546133935451508, -3.3359017372131348, -2.736828088760376, -3.658785343170166, -1.797024130821228, -1.1880947351455688, -3.506362199783325, -2.593973159790039], 
#         [14.568373680114746, -3.6436944007873535, -3.867562770843506, -5.442567348480225, -5.987629413604736, -5.067170143127441, -2.0206010341644287, -2.364003896713257, -5.770744800567627, -0.21749144792556763, -2.733248710632324, -3.5707733631134033, -3.5132124423980713, -3.5221498012542725, -2.3484928607940674, -3.8073291778564453, -3.4975779056549072], 
#         [15.901341438293457, -4.586617469787598, -4.657439708709717, -5.721152305603027, -6.836240291595459, -4.63149356842041, -2.8958609104156494, -2.0163679122924805, -5.875938892364502, -0.5394192337989807, -3.441737413406372, -3.1685564517974854, -3.772259473800659, -2.7859272956848145, -2.8951101303100586, -4.296492099761963, -3.692574977874756], 
#         [14.264222145080566, -3.7461209297180176, -4.285037994384766, -4.663211345672607, -5.726398944854736, -5.214822292327881, -2.6472043991088867, -1.648926854133606, -5.491762638092041, -0.17488327622413635, -3.3382465839385986, -2.34991192817688, -3.45076847076416, -2.6641130447387695, -1.8438787460327148, -3.0825507640838623, -3.012169361114502], 
#         [14.51372241973877, -4.046928882598877, -4.566728591918945, -4.428096294403076, -5.638655185699463, -5.578115463256836, -2.9144256114959717, -1.6396162509918213, -5.661402225494385, -0.35932809114456177, -3.7803821563720703, -2.451083183288574, -3.4790964126586914, -2.702164649963379, -1.8028924465179443, -3.1795928478240967, -3.086617946624756], 
#         [14.726181983947754, -5.093885898590088, -4.14469575881958, -5.206202983856201, -5.853297710418701, -4.589465141296387, -2.9251327514648438, -2.2416436672210693, -5.370000839233398, -0.5764406323432922, -3.462606430053711, -2.99924635887146, -3.4506287574768066, -2.2180116176605225, -1.987701654434204, -3.6380770206451416, -3.053532123565674], 
#         [12.942381858825684, -2.6757662296295166, -4.070926189422607, -4.246172904968262, -5.145177364349365, -4.000545024871826, -2.1046853065490723, -2.3647730350494385, -4.445437908172607, -0.3768905997276306, -2.723762035369873, -2.7431678771972656, -3.2990641593933105, -2.8187756538391113, -2.309644937515259, -3.6955182552337646, -3.1725690364837646], 
#         [14.703876495361328, -3.5835986137390137, -3.506204605102539, -6.800256252288818, -6.427453517913818, -2.912055253982544, 0.49381327629089355, -5.684810638427734, -6.659465789794922, 0.5542798042297363, -4.0550713539123535, -5.615508079528809, -3.5979673862457275, -4.609960079193115, -3.844468593597412, -4.942373752593994, -5.34766149520874], 
#         [1.0666639804840088, -4.140100479125977, 2.461851119995117, -9.811736106872559, 0.24756160378456116, -2.4496004581451416, 16.547163009643555, -10.0376558303833, -5.110496997833252, 4.4134087562561035, 2.1901865005493164, -14.109640121459961, 3.751148223876953, -12.477275848388672, -2.9810357093811035, -8.973225593566895, -6.377708911895752], 
#         [2.922731399536133, -8.530973434448242, -6.084386348724365, 0.1854173094034195, -7.159914970397949, -6.21536922454834, 4.250897407531738, 6.050698757171631, -12.893742561340332, 16.198373794555664, -5.474532604217529, -3.931234121322632, -4.800064563751221, -4.039795398712158, 4.094758033752441, -0.4106030762195587, 2.176970958709717], 
#         [5.182017803192139, -7.71131706237793, -3.3866984844207764, -3.1003758907318115, -8.654664039611816, -5.613524913787842, 2.605041980743408, 2.5310633182525635, -10.897804260253906, 14.06755542755127, -4.631836414337158, -7.724557876586914, -3.7085371017456055, -4.843715190887451, 2.4429731369018555, -3.21380615234375, -0.3682885468006134], 
#         [2.083817958831787, -7.142880439758301, -1.7480663061141968, -2.5343449115753174, -7.711868762969971, -7.0847320556640625, 4.4489946365356445, 5.892462730407715, -13.648896217346191, 17.93766212463379, -4.168127536773682, -5.115943908691406, -3.0955491065979004, -3.3887338638305664, 5.164085388183594, 0.20811089873313904, 3.631765365600586], 
#         [2.5991177558898926, -6.062826156616211, -9.895054817199707, 3.8987877368927, -0.17703494429588318, -3.337202548980713, -9.626958847045898, 17.218387603759766, -8.8556489944458, 5.524770736694336, -12.066627502441406, 0.8497487306594849, -9.396035194396973, 4.12946081161499, -0.5887815952301025, -6.054268836975098, -3.289123773574829], 
#         [13.898083686828613, -5.210517883300781, -5.403012752532959, -5.456071376800537, -8.626591682434082, -5.142745018005371, -6.148175239562988, -0.12574496865272522, -6.028229713439941, 2.2103958129882812, -6.025509357452393, -4.109138488769531, -3.646195411682129, -1.9831873178482056, -0.7351645231246948, -5.367005348205566, -3.3596596717834473], 
#         [-2.077512264251709, 13.944916725158691, -5.919556140899658, -4.261636257171631, 3.811542510986328, -4.736565113067627, -1.3389757871627808, 1.5511133670806885, -2.9095020294189453, -4.15151309967041, 0.6051821708679199, 2.1097514629364014, -3.25260853767395, -6.565557956695557, -6.2727837562561035, -4.010273456573486, -7.4264068603515625], 
#         [14.323380470275879, -2.660008192062378, -5.772607326507568, -5.984577655792236, -7.0229878425598145, -6.48158073425293, -6.2296037673950195, -0.15048182010650635, -7.404111385345459, -0.9706404209136963, -6.597461223602295, -0.7099595069885254, -4.815859794616699, -2.6618621349334717, -3.5160741806030273, -4.657401084899902, -3.8576176166534424]
#     ], 
#     'mask': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 
#     'tags': ['U-ORG', 'O', 'O', 'U-ORG', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-ORG', 'I-ORG', 'I-ORG', 'I-ORG', 'L-ORG', 'O', 'U-LOC', 'O'], 
#     'words': ['AllenNLP', 'is', 'a', 'PyTorch', '-', 'based', 'natural', 'language', 'processing', 'library', 'developed', 'at', 'the', 'Allen', 'Institute', 'for', 'Artificial', 'Intelligence', 'in', 'Seattle', '.']
# }