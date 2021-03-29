## SUmmary of the paper

### Intro 

    1. Already ML techniques exists to use the traiditional signal processingg(SP) and ML techniques.Many of these techniques show good accuracy for one eproblem but fial in performing accuractely for others e.g.: they classify seizure vs non-sezure with a good accuracy but show poor performance in case of norma vs icatl vs inter-ictal.

    2. Challenging problem due to:
        1. A generalized model does not exist which can classify binary as well as ternary problem.
        2. Less available labelled data
        3. Low accuracy.

    3. EEG Signal contians a low-frequency features with long time-period and high-frequency features with a short time period.

### Model and Architecture Description 
    
    1. Base
    An EEG recording is a 1D-Signal , we take a pyramidical 1D-CNN(P-1D-CNN) model for detecing epilepsy,whcih comprises of far fewer number of learnable parameters.

    2. Experts Model:
        Using tained P-1D-CNN models as experts,er design a system as an ensemble of P-1D-CNN models,ehich employs majority vite strategy to fusr the local decisionsfor detecting epilepsy.
    
    3. The proposed system takes an EEG signal ,segment it with fixed-size sliding window,and pass the sub-signals to base P-1D-CNN models, the process them and give the local decisions to the majority-vote module.

    4. At end ,the majority-vote module takes the final decision.It outperforms the other techniques for different problems conecring epilepsy detection.

    5. Main contributions:
        1. Data augmentation
        2. Automatic system based on an ensemble of P-1D-CNN depp models for binary as weel as ternary EEG-signals classification.
        3. A new approach for structutring deep 1D-CNN model.
        4. Thorouh evalution of the augmentation schemes and the deep models for detecting differnt epilepsy cases.




