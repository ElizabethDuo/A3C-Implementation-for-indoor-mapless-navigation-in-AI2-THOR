# A3C Implementation for indoor mapless navigation in AI2-THOR
A tensorflow implementation to train malpess navigation policy in AI2-THOR, an indoor simulator.<br>
This is a cpu version.

## Requirements<br>
  Python 2.7<br>
  Tensorflow 1.12<br>
  AI2-THOR<br>

## Train
* Modify paraments<br>
  >`line24`:change the number of trainning `episodes`<br>
  >`line25`:change the number of `steps` per episode<br>
  >`line212`:change the scene an agent navigates in and the target object . The default scene is `Scene201`, and the target is `GarbageCan`.<br>
  >`line248`:change the initial position in `x` and `z`.<br>
  >`line249`:change the initial rotation in `rotation`.<br>
  >`line426`: change the number of workers in A3C algorithms.

* Run <br>
  > `python A3C.py`

## PLOT
* Vertical view of Scene201<br>
  run `third-camera.py`<br>
  You'll get nine third-party cameras which will automatically save their vertical views cover the whole scene.<br>
  Then you'll know what's the scene looks like through these pictures.<br>
  The position of each camera can be different according to the specific size of each scecne, change it in `event0` to `event8` if necessary.<br><br>
  <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image8.jpg" width="150" alt="image8">
  <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image7.jpg" width="150" alt="image7">
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image6.jpg" width="150" alt="image6"><br>
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image5.jpg" width="150" alt="image5">
  <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image4.jpg" width="150" alt="image4">
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image3.jpg" width="150" alt="image3"><br>
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image2.jpg" width="150" alt="image2">
  <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image1.jpg" width="150" alt="image1">
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/image0.jpg" width="150" alt="image0"><br>

  
* Trainning results<br>
  There will be 3 parts visualized your trainning in each episode: agent's trajetory,distance form target and rewards per step.<br>
  The upper left pitcure showed the trajetory of the agent.The blue point is start pisition and the green point is where target object located. The position of the agent in one episode is shown in red from light colour to dark colour.<br><br>
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/reward%20episode-3-A3C4.png" width="375" alt="1"><br><br>
   The navigation succeed when distance between agent and target object less than 1.1 .<br><br>
   <img src = "https://github.com/ElizabethDuo/A3C-Implementation-for-indoor-mapless-navigation-in-AI2-THOR/blob/master/example%20pics/reward%20episode-16-A3C4.png" width="375" alt="1"><br><br>
   
## Reference
  [allenai/ai2thor](https://github.com/allenai/ai2thor)<br>
  [MorvanZhou/Reinforcement-learning-with-tensorflow
](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow)<br>
  [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/pdf/1602.01783.pdf)<br>

