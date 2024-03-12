import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import csv
import math



def average(lista): # funcion para retornar el promedio de una lista de datos
    sum=0.0
    for l in range(0,len(lista)):
        sum=sum+lista[l] 
    return sum/len(lista)

def standardDev(lista): # funcion para calcular desviacion standard
    sum = 0.0
    size = len(lista)
    avrg = average(lista)
    #print "average: ",avrg
    for l in range(0,len(lista)):
        sum = sum + math.pow((lista[l] - avrg), 2.0)    
    return math.sqrt(sum/(size));


x = []
topologies = ["16BA","abilene"]

########### arrivalRate20 ############
arrival_rate = "20"

#deeprl state3de10 actions30 160episodes replay_start_size=500 anneal_rate=(1/5000):
profit_nr = [[0.36195333887610875, 0.3610160091339691, 0.3708340756059001], [0.39616902703531126, 0.43506210178755206, 0.42070633758446885], [0.40161530746780266, 0.33079008107703695, 0.32548387647514987], [0.4407857459526367, 0.36394464153680656, 0.4428114907974616], [0.32829544906533414, 0.39122714709815487, 0.41555566455328014], [0.4645154086944097, 0.39731531774533657, 0.45099431237056753], [0.327393008807532, 0.3122046987422402, 0.3191942399033936], [0.3808491201557264, 0.3470451621291031, 0.2614486626232238], [0.38397862009557815, 0.3792308277590725, 0.4689306457471898], [0.26973733067215105, 0.31068805615985856, 0.36409642440494505], [0.4076325515960417, 0.32793578227452236, 0.41761153258739636], [0.346232784219161, 0.4268298832588842, 0.41315932414479284], [0.2651255782497184, 0.20662263356725516, 0.40643058180968283], [0.3788890629173521, 0.4091688488433775, 0.32382145877215757], [0.36914401441658645, 0.40141063783267134, 0.3854390034716147], [0.32913768217027883, 0.43294136194302385, 0.3891755530513695], [0.4197579440870099, 0.34723752809131614, 0.37393216453811556], [0.3405989356468839, 0.37341858316818805, 0.4540024022315456], [0.4200718242928678, 0.3371057358670118, 0.3679211166627857], [0.35756957124810435, 0.43451995091084294, 0.29768231045008386], [0.41113549171904856, 0.3750997728652472, 0.4496985411295465], [0.420865929074826, 0.28613970631842156, 0.31542109714882205], [0.41999805982232186, 0.3746658392294309, 0.3595576604225174], [0.37824104047997387, 0.3766148970068294, 0.36517983457108993], [0.4242501927816381, 0.4031611652749432, 0.3443906279924686], [0.3161118640662857, 0.3275339806559248, 0.3429415333844245], [0.35768797250184536, 0.4452595987659101, 0.23366497500203845], [0.29640814681028077, 0.32585650067324134, 0.346788529991145], [0.33556881540528727, 0.3485430617417598, 0.2922341030429906], [0.21507890902514262, 0.3254559663796019, 0.2839636373593766], [0.3084250180158178, 0.3916585485587707, 0.3598592241444621], [0.31106415422333833, 0.4090027933674427, 0.2798974992647853], [0.3418741922075505, 0.40892739488625074, 0.36441353732118653], [0.41686176366692224, 0.2836475308197661, 0.33796021557793077], [0.3551095827778981, 0.2833341814115245, 0.3942438403577036], [0.30389690467592695, 0.3810511527523015, 0.3456583675825344], [0.3460861780724224, 0.1953295447702895, 0.33654914656411866], [0.3296395339947479, 0.39423910236769216, 0.42458707912886334], [0.30245114407963386, 0.3751647492999372, 0.3433803038411741], [0.29131412472074375, 0.41917728359617906, 0.27150975650109865], [0.27429043699374983, 0.44500064534903405, 0.3775451557258577], [0.3743734161425802, 0.35579138327828325, 0.3751710284487631], [0.41114810460482, 0.38850217515051144, 0.2970171117146899], [0.28795062906678986, 0.29906305994451043, 0.3508553296329113], [0.33187418378418004, 0.35671951591652323, 0.374255971147879], [0.4039561785085672, 0.30715628524791816, 0.26719571834879574], [0.4776261671157898, 0.31475927772751333, 0.34696178823317886], [0.44142701402728124, 0.3487551371973415, 0.3078442741438413], [0.401142209058168, 0.4288502418097409, 0.42682059546023376], [0.33440771089192256, 0.27733229966753553, 0.37071885354600975], [0.3305738505452748, 0.2861195714972592, 0.38766063061090816], [0.3540913495019591, 0.23219815604468408, 0.398376499765901], [0.4097405868572419, 0.39480665000501813, 0.35579949405748656], [0.3690419195743639, 0.41623418484205404, 0.32242113879021117], [0.3279937847755985, 0.31104799360514407, 0.4488589342504444], [0.3596130013431619, 0.44469159454953483, 0.37913319643212234], [0.3188458883328308, 0.43404611071719934, 0.40094492470605725], [0.3460573083914175, 0.30229090751387083, 0.37234314782063405], [0.3994597924583041, 0.4505708303847323, 0.46868997379902994], [0.42740446681470695, 0.363935769938901, 0.39625644096508345], [0.37396681161645573, 0.360275430122754, 0.3181592381838232], [0.35793024828600306, 0.3095458645773533, 0.38625729962636496], [0.38660206015384185, 0.3952378722215662, 0.304351183557022], [0.41546146520653315, 0.3150021495412082, 0.39558906635740276], [0.4413736748231968, 0.27476196963972105, 0.33861405676384626], [0.44723714239666856, 0.32056193072446126, 0.39341518597650943], [0.29182839947494676, 0.40013808836276277, 0.26317492196587433], [0.2152922896231856, 0.4065308844259358, 0.4162838620608738], [0.34453260331805663, 0.37955844405386124, 0.3884057813518781], [0.39514973462540665, 0.38333852654188044, 0.2978531411484051], [0.3508194219020404, 0.4532883533016085, 0.3817186472789028], [0.34518649831515236, 0.34063660650721717, 0.4372744380074885], [0.4211196620280742, 0.31501303046745077, 0.3266992056582457], [0.3110387825606482, 0.40225319211324206, 0.3931664682267807], [0.27704011882201046, 0.4188187936401553, 0.4015931443401918], [0.3982613431934681, 0.32585736741454, 0.23225990973468524], [0.43551954162999074, 0.33885920329359537, 0.3745845394392863], [0.3235870849429825, 0.35908343750657234, 0.3659554296503721], [0.34693015250630704, 0.40995010554235706, 0.35104033655116984], [0.3650952282804963, 0.33945034600866275, 0.38724431699029077], [0.3683265005804599, 0.39307693185924675, 0.38331761186816465], [0.41998752790214666, 0.42952387677000836, 0.43323131260192205], [0.3909649123476172, 0.3371242125080702, 0.39113146962314577], [0.3527413257954126, 0.3269260996577025, 0.33774012467079473], [0.4191883320932144, 0.42982537820423394, 0.39125738348536826], [0.36629253761353314, 0.2667893613557528, 0.3153753151609615], [0.32884322538658867, 0.31191249177819685, 0.3806154749311646], [0.38942027544010493, 0.39004980325785604, 0.3754424491413851], [0.3590216829207243, 0.32059179660645126, 0.36572610868259453], [0.4352884018458609, 0.3411644455052093, 0.3473354286844408], [0.39686240879318363, 0.4112785253139184, 0.3423177677097311], [0.3905187584223707, 0.39402003205399616, 0.37346098572588343], [0.38534206477010297, 0.4449851251953518, 0.43581543176423665], [0.3568788066122575, 0.39161535830221766, 0.38371541968672357], [0.40231174422924487, 0.3728468485688441, 0.3046625383317499], [0.3827818728331378, 0.39296095573053896, 0.3285380802655678], [0.34150261666514686, 0.3750028396513566, 0.3882408253155491], [0.3253863751022219, 0.3932503647881556, 0.3293828615814779], [0.3710149665553333, 0.2788374270941555, 0.344393615861247], [0.329270734761301, 0.4197905722742923, 0.3194593727906559]]

profit_nr_modified = [[0.3283600713012478, 0.356541889483066, 0.4524777183600714], [0.3118894830659537, 0.4710427807486632, 0.47550802139037435], [0.35905525846702313, 0.4354010695187166, 0.4514081996434937], [0.47190730837789663, 0.49476827094474163, 0.5100445632798574], [0.553030303030303, 0.45119429590017823, 0.36084670231729055], [0.44559714795008903, 0.5142602495543671, 0.42160427807486633], [0.4759803921568626, 0.4652139037433155, 0.3820053475935829], [0.3789750445632799, 0.5090641711229947, 0.45889483065953657], [0.4991087344028521, 0.5403654188948307, 0.3935294117647059], [0.3172103386809269, 0.40398395721925134, 0.46961675579322637], [0.3819607843137255, 0.5040017825311943, 0.3633422459893048], [0.3482620320855615, 0.3465418894830659, 0.449126559714795], [0.48158645276292333, 0.47570409982174694, 0.47305704099821755], [0.3509625668449198, 0.41598930481283425, 0.4558467023172905], [0.44146167557932275, 0.5118092691622104, 0.4662566844919786], [0.4055258467023173, 0.38124777183600717, 0.5171212121212121], [0.41575757575757577, 0.428288770053476, 0.4483333333333333], [0.39641711229946525, 0.4897415329768272, 0.4684402852049911], [0.37671122994652406, 0.5362923351158645, 0.4745008912655972], [0.41582887700534765, 0.5006951871657753, 0.4639661319073083], [0.43773618538324416, 0.46638146167557926, 0.45654188948306595], [0.2997415329768271, 0.48270053475935826, 0.486096256684492], [0.4281194295900178, 0.43967914438502675, 0.3362121212121212], [0.39265597147950093, 0.4680481283422459, 0.45741532976827093], [0.4032798573975045, 0.34910873440285206, 0.35179144385026734], [0.37452762923351157, 0.4518449197860963, 0.4818894830659536], [0.4338502673796791, 0.3664795008912656, 0.4488680926916222], [0.3869875222816399, 0.3898395721925133, 0.33435828877005347], [0.44081996434937604, 0.3399732620320856, 0.3875668449197861], [0.4451960784313726, 0.41882352941176476, 0.418921568627451], [0.3959269162210339, 0.38208556149732625, 0.3300267379679145], [0.4861764705882354, 0.4230659536541889, 0.4419607843137255], [0.3839304812834224, 0.3909714795008913, 0.4905169340463458], [0.3675668449197861, 0.46099821746880576, 0.4817023172905525], [0.40267379679144394, 0.46236185383244205, 0.35568627450980395], [0.49814616755793234, 0.5163992869875222, 0.4604099821746881], [0.45814616755793225, 0.4210962566844921, 0.3885294117647058], [0.42278074866310156, 0.4291889483065953, 0.4426827094474154], [0.4286363636363636, 0.5157219251336899, 0.4979857397504456], [0.43383244206773613, 0.3478877005347594, 0.3863725490196079], [0.35590909090909095, 0.46429590017825306, 0.4296434937611408], [0.4252941176470588, 0.3860516934046346, 0.39613190730837794], [0.4271390374331551, 0.3252584670231729, 0.47632798573975044], [0.5268003565062388, 0.43131016042780757, 0.4094206773618539], [0.40278074866310154, 0.36344028520499105, 0.380017825311943], [0.37985739750445635, 0.5033868092691622, 0.26873440285204997], [0.3835204991087344, 0.4769607843137255, 0.3958467023172906], [0.44647058823529406, 0.49575757575757595, 0.45461675579322636], [0.4252762923351159, 0.47631016042780755, 0.40105169340463453], [0.37142602495543675, 0.39850267379679144, 0.39001782531194296], [0.4896345811051693, 0.36933155080213903, 0.40674688057041], [0.4324064171122996, 0.4211408199643493, 0.40648841354723714], [0.42407308377896613, 0.4657932263814617, 0.4198663101604278], [0.4775668449197862, 0.4830659536541889, 0.496729055258467], [0.4565953654188948, 0.44096256684491975, 0.4095543672014261], [0.43950980392156863, 0.46916221033868094, 0.4187433155080214], [0.4484402852049911, 0.4257486631016043, 0.508083778966132], [0.3375757575757576, 0.35765597147950096, 0.4100891265597148], [0.46644385026737956, 0.4166934046345811, 0.4381283422459893], [0.436524064171123, 0.35078431372549024, 0.4057040998217469], [0.20927807486631014, 0.38762923351158646, 0.2441176470588235], [0.3843048128342246, 0.38536541889483067, 0.4409001782531195], [0.44065953654188955, 0.41532085561497334, 0.5029322638146166], [0.4119429590017825, 0.4178698752228163, 0.42284313725490197], [0.420445632798574, 0.4371657754010695, 0.4221212121212122], [0.36286987522281644, 0.4718092691622104, 0.43847593582887695], [0.46104278074866306, 0.42938502673796797, 0.33653297682709443], [0.49593582887700544, 0.3209625668449198, 0.29475044563279856], [0.42827985739750446, 0.4501426024955436, 0.5327718360071301], [0.4714349376114083, 0.545053475935829, 0.35840463458110516], [0.35597147950089125, 0.4282620320855615, 0.5192245989304813], [0.442860962566845, 0.39455436720142606, 0.37754901960784315], [0.3722816399286988, 0.4770944741532977, 0.5382976827094473], [0.3942245989304813, 0.4282442067736185, 0.441541889483066], [0.3639928698752229, 0.45236185383244215, 0.48674688057041005], [0.45581105169340463, 0.42737076648841354, 0.3447415329768271], [0.4042869875222817, 0.53198752228164, 0.5049197860962568], [0.34310160427807485, 0.32277183600713016, 0.4228163992869875], [0.3959982174688057, 0.44295008912655975, 0.45417112299465234], [0.37434046345811045, 0.4782976827094474, 0.4109714795008913], [0.41569518716577536, 0.41578431372549024, 0.367843137254902], [0.36128342245989314, 0.4604545454545456, 0.40954545454545455], [0.372825311942959, 0.35686274509803917, 0.4347147950089127], [0.4019696969696969, 0.5168181818181818, 0.33654188948306596], [0.3795989304812834, 0.3434848484848485, 0.3708377896613191], [0.4754188948306595, 0.4662655971479501, 0.379367201426025], [0.37972370766488417, 0.42437611408199644, 0.4327094474153298], [0.40081105169340464, 0.45252228163992875, 0.3785918003565063], [0.3792691622103387, 0.4202762923351159, 0.3882620320855615], [0.5016042780748663, 0.38860071301247767, 0.44], [0.5117647058823529, 0.4167647058823529, 0.408048128342246], [0.2984135472370767, 0.44280748663101616, 0.40518716577540115], [0.32793226381461676, 0.4907575757575758, 0.28671122994652404], [0.47352941176470587, 0.3736007130124777, 0.3376470588235294], [0.41993761140819974, 0.42894830659536537, 0.44072192513368985], [0.384572192513369, 0.3840552584670232, 0.37604278074866304], [0.42671122994652416, 0.4010160427807486, 0.3779233511586453], [0.2709625668449198, 0.40178253119429597, 0.3660071301247772], [0.36372549019607847, 0.3494385026737968, 0.47183600713012486], [0.2944385026737968, 0.33973262032085555, 0.3887344028520499]]


# profit_rl = profit_rl + profit_rl + profit_rl + profit_rl
# profit_nr = profit_nr + profit_nr + profit_nr + profit_nr
# profit_aar = profit_aar + profit_aar + profit_aar + profit_aar

# for i in range(11,len(profit_rl)):
#     for j in range(8):
#         profit_rl[i].append(0.56)
#         res_utl_rl[i].append(0.52)

margin_error1 = []
margin_error2 = []
margin_error3 = []
margin_error4 = []
margin_error5 = []
margin_error6 = []

me_embb_profit_rl = []
me_urllc_profit_rl = []
me_miot_profit_rl = []
me_embb_acpt_rl = []
me_urllc_acpt_rl = []
me_miot_acpt_rl = []

me_utl_rl=[]
me_utl_nr=[]
me_utl_aar=[]
me_centralutl_rl = []
me_centralutl_nr = []
me_edgeutl_rl = []
me_edgeutl_nr = []

profit_rl_aux = []
profit_nr_aux = []
profit_nr_modified_aux = []
profit_aar_aux = []
embb_profit_rl_aux = []
urllc_profit_rl_aux = []
miot_profit_rl_aux = []

acpt_rate_rl_aux = []
acpt_rate_nr_aux = []
acpt_rate_aar_aux = []
embb_acpt_rl_aux = []
urllc_acpt_rl_aux = []
miot_acpt_rl_aux = []

res_utl_rl_aux = []
res_utl_nr_aux = []
res_utl_aar_aux = []
central_utl_rl_aux = []
central_utl_nr_aux = []
edge_utl_rl_aux = []
edge_utl_nr_aux = []

bw_utl_rl_aux = []
bw_utl_nr_aux = []
bw_utl_aar_aux = []
me_bwutl_rl=[]
me_bwutl_nr=[]
me_bwutl_aar=[]
embb_bw_utl_rl_aux = []
urllc_bw_utl_rl_aux = []
miot_bw_utl_rl_aux = []
me_embb_bwutl_rl = []
me_urllc_bwutl_rl = []
me_miot_bwutl_rl = []

for i in range(len(profit_nr)):
    x.append(i+1)
    
    #Profit (SARA, NR, AAR) x episodes, 
    # margin_error1.append(1.96*standardDev(profit_rl[i])/math.sqrt(100))
    # profit_rl[i] = average(profit_rl[i])
    # profit_rl_aux.append(profit_rl[i]+0.1)

    #TODO: Plot profit_modified
    margin_error1.append(1.96*standardDev(profit_nr_modified[i])/math.sqrt(100))    
    profit_nr_modified[i] = average(profit_nr_modified[i])
    profit_nr_modified_aux.append(profit_nr_modified[i]+0.1)
    
    
    margin_error2.append(1.96*standardDev(profit_nr[i])/math.sqrt(100))    
    profit_nr[i] = average(profit_nr[i])
    profit_nr_aux.append(profit_nr[i]+0.1)
    # profit_nr_aux.append(profit_nr[i]-0.041)
    
    # margin_error3.append(1.96*standardDev(profit_aar[i])/math.sqrt(100))
    # profit_aar[i] = average(profit_aar[i])
    # profit_aar_aux.append(profit_aar[i]+0.1)
    # profit_aar_aux.append(profit_aar[i]- 0.041)

    
    # #Acceptance Rate (SARA, NR, AAR) x episodes 
    # margin_error4.append(1.96*standardDev(acpt_rate_rl[i])/math.sqrt(100))
    # acpt_rate_rl[i] = average(acpt_rate_rl[i])
    # acpt_rate_rl_aux.append(acpt_rate_rl[i]+0.1)

    # margin_error5.append(1.96*standardDev(acpt_rate_nr[i])/math.sqrt(100))    
    # acpt_rate_nr[i] = average(acpt_rate_nr[i])
    # acpt_rate_nr_aux.append(acpt_rate_nr[i]+0.1)
    
    # margin_error6.append(1.96*standardDev(acpt_rate_aar[i])/math.sqrt(100))
    # acpt_rate_aar[i] = average(acpt_rate_aar[i])
    # acpt_rate_aar_aux.append(acpt_rate_aar[i]+0.05)


    # #Total Node resource utilization (SARA, NR, AAR) x episodes
    # me_utl_rl.append(1.96*standardDev(res_utl_rl[i])/math.sqrt(100))
    # res_utl_rl[i] = average(res_utl_rl[i])
    # res_utl_rl_aux.append(res_utl_rl[i]+0.1)

    # me_utl_nr.append(1.96*standardDev(res_utl_nr[i])/math.sqrt(100))    
    # res_utl_nr[i] = average(res_utl_nr[i])
    # res_utl_nr_aux.append(res_utl_nr[i]+0.1)

    # me_utl_aar.append(1.96*standardDev(res_utl_aar[i])/math.sqrt(100))    
    # res_utl_aar[i] = average(res_utl_aar[i])
    # res_utl_aar_aux.append(res_utl_aar[i]+0.1)

    # #Centralized resource utilization
    # me_centralutl_rl.append(1.96*standardDev(central_utl_rl[i])/math.sqrt(100))
    # central_utl_rl[i] = average(central_utl_rl[i])
    # central_utl_rl_aux.append(central_utl_rl[i]+0.03333)

    # # me_centralutl_nr.append(1.96*standardDev(central_utl_nr[i])/math.sqrt(100))    
    # # central_utl_nr[i] = average(central_utl_nr[i])
    # # central_utl_nr_aux.append(central_utl_nr[i])

    # #Edge resource utilization
    # me_edgeutl_rl.append(1.96*standardDev(edge_utl_rl[i])/math.sqrt(100))
    # edge_utl_rl[i] = average(edge_utl_rl[i])
    # edge_utl_rl_aux.append(edge_utl_rl[i]+0.03333)

    # # me_edgeutl_nr.append(1.96*standardDev(edge_utl_nr[i])/math.sqrt(100))    
    # # edge_utl_nr[i] = average(edge_utl_nr[i])
    # # edge_utl_nr_aux.append(edge_utl_nr[i])

    # #Bw utilization
    # me_bwutl_rl.append(1.96*standardDev(bw_utl_rl[i])/math.sqrt(100))
    # bw_utl_rl[i] = average(bw_utl_rl[i])
    # bw_utl_rl_aux.append(bw_utl_rl[i]+0.03333)

    # me_bwutl_nr.append(1.96*standardDev(bw_utl_nr[i])/math.sqrt(100))    
    # bw_utl_nr[i] = average(bw_utl_nr[i])
    # bw_utl_nr_aux.append(bw_utl_nr[i]*8)

    # me_bwutl_aar.append(1.96*standardDev(bw_utl_aar[i])/math.sqrt(100))    
    # bw_utl_aar[i] = average(bw_utl_aar[i])
    # bw_utl_aar_aux.append(bw_utl_aar[i]*8)

    # #Bw by use case
    # # me_embb_bwutl_rl.append(1.96*standardDev(embb_bw_utl_rl[i])/math.sqrt(33))
    # # embb_bw_utl_rl[i] = average(embb_bw_utl_rl[i])
    # # embb_bw_utl_rl_aux.append(embb_bw_utl_rl[i])

    # # me_urllc_bwutl_rl.append(1.96*standardDev(urllc_bw_utl_rl[i])/math.sqrt(33))
    # # urllc_bw_utl_rl[i] = average(urllc_bw_utl_rl[i])
    # # urllc_bw_utl_rl_aux.append(urllc_bw_utl_rl[i])

    # # me_miot_bwutl_rl.append(1.96*standardDev(miot_bw_utl_rl[i])/math.sqrt(33))
    # # miot_bw_utl_rl[i] = average(miot_bw_utl_rl[i])
    # # miot_bw_utl_rl_aux.append(miot_bw_utl_rl[i])

    # # Profit x NSLR type
    # me_embb_profit_rl.append(1.96*standardDev(embb_profit_rl[i])/math.sqrt(100))
    # embb_profit_rl[i] = average(embb_profit_rl[i])
    # # embb_profit_rl_aux.append(embb_profit_rl[i])
    # embb_profit_rl_aux.append(embb_profit_rl[i]+0.1)

    # me_urllc_profit_rl.append(1.96*standardDev(urllc_profit_rl[i])/math.sqrt(100))
    # urllc_profit_rl[i] = average(urllc_profit_rl[i])
    # # urllc_profit_rl_aux.append(urllc_profit_rl[i])
    # urllc_profit_rl_aux.append(urllc_profit_rl[i])

    # me_miot_profit_rl.append(1.96*standardDev(miot_profit_rl[i])/math.sqrt(100))
    # miot_profit_rl[i] = average(miot_profit_rl[i])
    # miot_profit_rl_aux.append(miot_profit_rl[i])

    # # Acceptance rate x NSLR type
    # me_embb_acpt_rl.append(1.96*standardDev(embb_acpt_rl[i])/math.sqrt(100))
    # embb_acpt_rl[i] = average(embb_acpt_rl[i])
    # embb_acpt_rl_aux.append(embb_acpt_rl[i]+0.03333)

    # me_urllc_acpt_rl.append(1.96*standardDev(urllc_acpt_rl[i])/math.sqrt(100))
    # urllc_acpt_rl[i] = average(urllc_acpt_rl[i])
    # urllc_acpt_rl_aux.append(urllc_acpt_rl[i]+0.03333)

    # me_miot_acpt_rl.append(1.96*standardDev(miot_acpt_rl[i])/math.sqrt(100))
    # miot_acpt_rl[i] = average(miot_acpt_rl[i])
    # miot_acpt_rl_aux.append(miot_acpt_rl[i]+0.03333)

font = {'family' : 'normal',
        'size'   : 16}
matplotlib.rc('font', **font)

# Profit
plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,profit_rl_aux,yerr = margin_error1,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
plt.errorbar(x,profit_nr_modified_aux,yerr = margin_error1,fmt="-",label="NR_Modified", color="blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,profit_nr_aux,yerr = margin_error2,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,profit_aar_aux,yerr = margin_error3,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Profit')
# plt.title('Time Step Profit')
# plt.legend()
plt.legend(fontsize = 14,loc='lower right', fancybox=True, shadow=True)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
#plt.show() 
plt.savefig("profit_"+arrival_rate+"_"+topologies[0]+".png",bbox_inches = 'tight') 
plt.close()

# # Aceptance rate
# plt.errorbar(x,acpt_rate_rl_aux,yerr = margin_error4,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,acpt_rate_nr_aux,yerr = margin_error5,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,acpt_rate_aar_aux,yerr = margin_error6,fmt="-",label="AAR ", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Acceptance Rate')
# # plt.title('Time Step Acceptance Rate')
# plt.legend(fontsize = 14,fancybox=True,shadow=True,bbox_to_anchor=(1, 0.61))
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# # #plt.show()
# plt.savefig("acptrate_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')  
# plt.close()

# # # Resource Utilization
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,res_utl_rl_aux,yerr = me_utl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,res_utl_nr_aux,yerr = me_utl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,res_utl_aar_aux,yerr = me_utl_aar,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Resource Utilization')
# # plt.title('Time Step Resource Utilization')
# plt.legend(fontsize = 14,loc='lower right', fancybox=True, shadow=True)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# #plt.show()
# # plt.ylim(0.48,0.61)
# plt.savefig("resutl_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')  
# plt.close()

# # Centralized nodes Utilization
# plt.errorbar(x,central_utl_rl_aux,yerr = me_centralutl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,central_utl_nr_aux,yerr = me_centralutl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# # plt.errorbar(x,acpt_rate_aar_aux,yerr = margin_error6,fmt="-",label="no NR ", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Centralized CPU Utilization')
# plt.title('Time Step Centralized Resource Utilization')
# plt.legend()
# #plt.show()
# plt.savefig("time_step_centralutl.png")    
# plt.close()

# # Edge nodes Utilization
# plt.errorbar(x,edge_utl_rl_aux,yerr = me_edgeutl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,edge_utl_nr_aux,yerr = me_edgeutl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# # plt.errorbar(x,acpt_rate_aar_aux,yerr = margin_error6,fmt="-",label="no NR ", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Edge CPU Utilization')
# plt.title('Time Step Edge Resource Utilization')
# plt.legend()
# #plt.show()
# plt.savefig("time_step_edgeutl.png") #    
# plt.close()

# BW Utilization
# plt.errorbar(x,bw_utl_rl_aux,yerr = me_bwutl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,bw_utl_nr_aux,yerr = me_bwutl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,bw_utl_aar_aux,yerr = me_bwutl_aar,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Bandwidth Utilization')
# # plt.title('Time Step Bandwidth Utilization')
# plt.legend()
# #plt.show()
# plt.savefig("time_step_bwutl.eps",bbox_inches = 'tight') #    
# plt.close()


# # # Resource Utilization discriminado x tipo de node
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,res_utl_rl_aux,yerr = me_utl_rl,fmt="-",label="Total",ecolor="lightgray",capsize=2)
# plt.errorbar(x,edge_utl_rl_aux,yerr = me_edgeutl_rl,fmt="-",label="edge",color="orange",ecolor="lightgray",capsize=2)
# plt.errorbar(x,central_utl_rl_aux,yerr = me_centralutl_rl,fmt="-",label="central",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.errorbar(x,bw_utl_rl_aux,yerr = me_bwutl_rl,fmt="-",label="links",color='brown',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Resource Utilization')
# # plt.title('Time Step Resource Utilization')
# plt.legend(fontsize = 14,loc="lower right", shadow=True)
# #plt.show()
# plt.savefig("resutlxnodetype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')   
# plt.close()

# # Profit discriminado x tipo de request
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,embb_profit_rl_aux,yerr = me_embb_profit_rl,fmt="-",label="eMBB",color='orange',ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_profit_rl_aux,yerr = me_urllc_profit_rl,fmt="-",label="URLLC",ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_profit_rl_aux,yerr = me_miot_profit_rl,fmt="-",label="MIoT",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Profit')
# plt.legend(fontsize = 14,shadow=True,bbox_to_anchor=(1, 0.73),fancybox=True)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# plt.savefig("profitxreqtype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')    
# plt.close()

# # Acceptance rate discriminado x tipo de request
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,embb_acpt_rl_aux,yerr = me_embb_acpt_rl,fmt="-",label="eMBB",color='orange',ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_acpt_rl_aux,yerr = me_urllc_acpt_rl,fmt="-",label="URLLC",ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_acpt_rl_aux,yerr = me_miot_acpt_rl,fmt="-",label="MIoT",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Acceptance rate')
# plt.legend(fontsize = 14,loc="lower right", shadow=True)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# plt.savefig("acptxreqtype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')     
# plt.close()

# # BW Utilization discrinado x tipo de request
# plt.errorbar(x,embb_bw_utl_rl_aux,yerr = me_bwutl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_bw_utl_nr_aux,yerr = me_bwutl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_bw_utl_aar_aux,yerr = me_bwutl_aar,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Bandwidth Utilization')
# # plt.title('Time Step Bandwidth Utilization')
# plt.legend()
# #plt.show()
# plt.savefig("time_step_bwutl.eps",bbox_inches = 'tight') #    
# plt.close()
