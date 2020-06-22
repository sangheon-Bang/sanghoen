import pygame, sys
import time
import random
import slid
from game_state import GameState
from game import Game


class Pokemon_game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((720,480))
        self.clock=pygame.time.Clock()
        self.running=True
        self.inList=""
        self.text_name=""


    def load_text(self,file_name):
        inFp=None
        inFp=open('C:/Users/방상헌/Desktop/오픈소스프로젝트 과제/'+file_name+'.txt')
        self.inList=inFp.readlines()
        self.inList=list(map(lambda s: s.strip(),self.inList))
        inFp.close()


    def text(self,sentence1,sentence2):
        textbar_img.load()
        text_position1=(25,362)
        text_position2=(25,410)
        font=pygame.font.SysFont('malgungothic',30)
        text_line1 = font.render(str(sentence1), True, (0,0,0))
        self.screen.blit(text_line1, text_position1)
        text_line2 = font.render(str(sentence2), True, (0,0,0))
        self.screen.blit(text_line2, text_position2)
        self.wait_for_next_event()


    def text_ver2(self,sentence,x,y):
        text_position=(x,y)
        font=pygame.font.SysFont('malgungothic',30)
        text_line = font.render(str(sentence), True, (0,0,0))
        self.screen.blit(text_line, text_position)

        
    def text_ver3(self,sentence,width,height,x,y):
        font=pygame.font.SysFont('malgungothic',25)
        text_line = font.render(str(sentence), True, (0,0,0))
        text_position=text_line.get_rect()
        text_position.x=x
        text_position.y=y
        text_position.center=(text_position.x+width//2,text_position.y+height//2)
        self.screen.blit(text_line, text_position)


    def display_textbar(self,file_name):
        game.load_text(file_name)
        global textbar_img
        textbar_img = Animation("텍스트바.png",720,150,0,330)
        textbar_img.load()
        text_position1 = (25, 362)
        text_position2 = (25, 410)
        font=pygame.font.SysFont('malgungothic',30)
        if len(self.inList)<2:
            text_line1 = font.render(str(self.inList[0]), True, (0,0,0))
            self.screen.blit(text_line1, text_position1)
            text_line2 = font.render(str(self.inList[1]), True, (0,0,0))
            self.screen.blit(text_line2, text_position2)
            self.wait_for_next_event()
            textbar_img.disappear()
        else:
            text_line1 = font.render(str(self.inList[0]), True, (0,0,0))
            self.screen.blit(text_line1, text_position1)
            text_line2 = font.render(str(self.inList[1]), True, (0,0,0))
            self.screen.blit(text_line2, text_position2)
            self.wait_for_next_event()
            textbar_img.load()
            if len(self.inList)%2==0:
                for i in range(1,len(self.inList)//2):
                    text_line1 = font.render(str(self.inList[2*i]), True, (0,0,0))
                    self.screen.blit(text_line1, text_position1)
                    text_line2 = font.render(str(self.inList[2*i+1]), True, (0,0,0))
                    self.screen.blit(text_line2, text_position2)
                    self.wait_for_next_event()
                    textbar_img.load()
                textbar_img.disappear()    

            else:
                for i in range(1,len(self.inList)//2):
                    pygame.display.flip()
                    text_line1 = font.render(str(self.inList[2*i]), True, (0,0,0))
                    self.screen.blit(text_line1, text_position1)
                    text_line2 = font.render(str(self.inList[2*i+1]), True, (0,0,0))
                    self.screen.blit(text_line2, text_position2)
                    self.wait_for_next_event()
                    textbar_img.load()
                
                text_line1 = font.render(str(self.inList[len(self.inList)-1]), True, (0,0,0))
                self.screen.blit(text_line1, text_position1)
                text_line2 = font.render("", True, (0,0,0))
                self.screen.blit(text_line2, text_position2)
                self.wait_for_next_event()
                textbar_img.disappear()
            

    def wait_for_next_event(self):
        self.running=True
        button_sound=pygame.mixer.Sound("버튼.ogg")
        while self.running:
            pygame.display.flip()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    button_sound.play()
                    self.running = False


    def start_gamescreen(self):
        startscreen_img = Animation("임시시작화면.png",720,480,0,0)
        startscreen_img.load()
        game.wait_for_next_event()
        startscreen_img.disappear()

            



class Animation:
    
    def __init__(self,file_name,width,height,x_pos,y_pos):
        self.running=True
        self.file_name=file_name
        self.width=width
        self.height=height
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.image=pygame.image.load(self.file_name).convert_alpha()
        self.image=pygame.transform.scale(self.image,(self.width,self.height))

        self.rect=self.image.get_rect()
        self.rect.x=self.x_pos
        self.rect.y=self.y_pos

    def moveRight(self,pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels
        
    def moveUp(self,pixels):
        self.rect.y -= pixels
        
    def moveDown(self,pixels):
        self.rect.y += pixels

    def disappear(self):
        self.moveUp(1000)
        game.screen.blit(self.image,self.rect)
        self.rect.y += 1000

    def resize(self,width,height,x,y):
        self.image=pygame.image.load(self.file_name).convert_alpha()
        self.image=pygame.transform.scale(self.image,(width,height))
        game.screen.blit(self.image,(x,y))
        
    def load(self):
        game.screen.blit(self.image,self.rect)

    def transparency(self,i):
        self.image.fill((0,0,0,i))

    def fade_in_black(self,height):
        fade_in=pygame.Surface((720,height)).convert_alpha()
        pygame.display.flip() 
        i=255
        fade_in.fill((0,0,0,i))
        game.screen.blit(fade_in,(0,0))
        
        while self.running:
            self.load()
            i-=15
            if(i<0):
                self.running=False
            else:
                fade_in.fill((0,0,0,i))
                game.screen.blit(fade_in,(0,0))
                pygame.display.update()
                game.clock.tick(60)
        self.running=True

    def fade_out_black(self,height):
        fade_in=pygame.Surface((720,height)).convert_alpha()
        pygame.display.flip() 
        i=0
        fade_in.fill((0,0,0,i))
        game.screen.blit(fade_in,(0,0))
        
        while self.running:
            self.load()
            i+=15
            if(i>255):
                self.running=False
            else:
                fade_in.fill((0,0,0,i))
                game.screen.blit(fade_in,(0,0))
                pygame.display.update()
                game.clock.tick(60)
        self.running=True




class Button():
    def __init__(self,width,height,x,y):
        self.width=width
        self.height=height
        self.x=x
        self.y=y


    def getnext(self,pos):
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.height:
                return True




class Pokemon:
    def __init__(self,name,skill,HP_current,HP):
        self.name=name
        self.skill=skill
        self.HP_current=HP_current
        self.HP=HP
        

    def random_skill(self):
        self.enemy_skill=random.choice(self.skill)
        return self.enemy_skill



    
        


def battle():
    Raichu=Pokemon("라이츄",["볼트태클","와일드볼트","기합구슬","사이코키네시스"],180,180)
    Charizard=Pokemon("리자몽",["플레어드라이브","용의분노","분출","드래곤다이브"],220,220)    
    pokemon_list=["라이츄","리자몽"]
    poke_name=random.choice(pokemon_list)
    if poke_name=="라이츄":
        random_poke=Raichu
    elif poke_name=="리자몽":
        random_poke=Charizard
    global random_poke_img
    random_poke_img=Animation(random_poke.name+".png",200,200,-275,5)
    
    battle_sound.play(-1)
    init_screen.load()
    textbar_img.load()
    pygame.display.update()
    forest_img.load()
    forest_img.fade_in_black(480) 

    running=True
    while running:
        pygame.display.flip() 
        if(grass_img.rect.x<-600):
            running=False
        else:
            forest_img.load()        
            grass_img.moveDown(5)
            grass_img.moveLeft(20)
            grass_img.load()
            textbar_img.load() 
            pygame.display.update()
            game.clock.tick(60)


    running=True
    while running:
        pygame.display.flip()
        if(stage1.rect.x>360):
            running=False
        else:
            forest_img.load()
            stage1.moveRight(20)
            stage2.moveLeft(20)
            player_img_battle.moveLeft(20)
            random_poke_img.moveRight(20)
            stage1.load()
            stage2.load()
            player_img_battle.load()
            random_poke_img.load()
            textbar_img.load()
            pygame.display.update()
            game.clock.tick(60)


    pokename=random_poke.name
    mypokename="내포켓몬1"
    game.text("야생의 "+pokename+"이/가 나타났다","")


    running=True
    while running:
        pygame.display.flip()
        if(player_img_battle.rect.x<-200):
            running=False
        else:
            forest_img.load()
            player_img_battle.moveLeft(20)
            stage1.load()
            stage2.load()
            interface1.load()
            game.text_ver2(pokename,5,50)
            HP_bar_bg.load()
            HP_bar.load()
            interface2.load()
            game.text_ver2("피카츄",395,215)
            HP_bar2_bg.load()
            HP_bar2.load()
            poke_ball.resize(60,60,160,250)
            player_img_battle.load()
            random_poke_img.load()
            textbar_img.load()
            pygame.display.update()
            game.clock.tick(60)


    light.resize(20,20,190,250)
    pygame.display.update()
    time.sleep(0.05)
    light.resize(140,140,145,200)
    pygame.display.update()
    time.sleep(0.05)
    light.resize(230,230,115,165)
    pygame.display.update()
    time.sleep(0.15)
    forest_img.load()
    stage1.load()
    stage2.load()
    interface1.load()
    game.text_ver2(pokename,5,50)
    HP_bar_bg.load()
    HP_bar.load()
    interface2.load()
    game.text_ver2("피카츄",395,215)
    HP_bar2_bg.load()
    HP_bar2.load()
    player_img_battle.load()
    random_poke_img.load()
    my_poke.load()
    textbar_img.load()
    light.resize(140,140,145,200)
    pygame.display.update()
    time.sleep(0.1)
    forest_img.load()
    stage1.load()
    stage2.load()
    interface1.load()
    game.text_ver2(pokename,5,50)
    HP_bar_bg.load()
    HP_bar.load()
    interface2.load()
    game.text_ver2("피카츄",395,215)
    HP_bar2_bg.load()
    HP_bar2.load()
    player_img_battle.load()
    random_poke_img.load()
    my_poke.load()
    textbar_img.load()
    light.resize(20,20,190,250)
    pygame.display.update()
    time.sleep(0.2)
    forest_img.load()
    stage1.load()
    stage2.load()
    interface1.load()
    game.text_ver2(pokename,5,50)
    HP_bar_bg.load()
    HP_bar.load()
    interface2.load()
    game.text_ver2("피카츄",395,215)
    HP_bar2_bg.load()
    HP_bar2.load()
    player_img_battle.load()
    random_poke_img.load()
    my_poke.load()
    textbar_img.load()

        
    game.text("가라! 피카츄!","")



    
    battle=True
    running=True
    my_HP=180
    my_HP_current=180
    

    while battle:
        button=Animation("버튼.png",360,150,0,330)
        button2=Animation("버튼3.png",360,150,360,330)

        battle_button=Button(360,150,0,330)
        run_button=Button(360,150,360,330)

    
        while running:
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if battle_button.getnext(pos):
                        fight=True
                        running=False
                    if run_button.getnext(pos):
                        game.text("성공적으로 도망쳤다","")
                        battle_sound.stop()
                        fight=False
                        battle=False
                        running=False
                        
                        
                else:
                    button.load()
                    button2.load()
                    game.text_ver2("싸운다",130,387)
                    game.text_ver2("도망친다",480,387)
                    pygame.display.update()
                    game.clock.tick(60)

        button_skill1=Animation("버튼4.png",180,150,0,330)
        button_skill2=Animation("버튼4.png",180,150,180,330)
        button_skill3=Animation("버튼4.png",180,150,360,330)
        button_skill4=Animation("버튼4.png",180,150,540,330)

    
        skill1_button=Button(180,150,0,330)
        skill2_button=Button(180,150,180,330)
        skill3_button=Button(180,150,360,330)
        skill4_button=Button(180,150,540,330)

        
        
        while fight:
            
            pika_skill_list=["이판사판태클","볼트태클","십만볼트","번개"]
   
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if skill1_button.getnext(pos):
                        battle_cycle(pokename,pika_skill_list[0])
                        random_poke.HP_current-=30
                        
                        if random_poke.HP_current<=0:
                            random_poke.HP_current=0
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            battle=battle_win(pokename) 
                        else:
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            pygame.display.update()
                            
                            battle_cycle2(random_poke.name,random_poke.random_skill())

                            if random_poke.enemy_skill=="볼트태클":
                                my_HP_current-=70
                            elif random_poke.enemy_skill=="와일드볼트":
                                my_HP_current-=90
                            elif random_poke.enemy_skill=="기합구슬":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="사이코키네시스":
                                my_HP_current-=80
                            elif random_poke.enemy_skill=="플레어드라이브":
                                my_HP_current-=100
                            elif random_poke.enemy_skill=="용의분노":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="분출":
                                my_HP_current-=40
                            elif random_poke.enemy_skill=="드래곤다이브":
                                my_HP_current-=120
                            
                            
                            if my_HP_current<=0:
                                my_HP_current=0
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                battle=battle_lose(pokename)
                             
                            else:
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                pygame.display.update()
                            
                        running=True
                        fight=False

                    
                    if skill2_button.getnext(pos):
                        battle_cycle(pokename,pika_skill_list[1])
                        random_poke.HP_current-=70

                        if random_poke.HP_current<=0:
                            random_poke.HP_current=0
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            battle=battle_win(pokename) 
                        else:
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            pygame.display.update()
                            
                            battle_cycle2(random_poke.name,random_poke.random_skill())

                            if random_poke.enemy_skill=="볼트태클":
                                my_HP_current-=70
                            elif random_poke.enemy_skill=="와일드볼트":
                                my_HP_current-=90
                            elif random_poke.enemy_skill=="기합구슬":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="사이코키네시스":
                                my_HP_current-=80
                            elif random_poke.enemy_skill=="플레어드라이브":
                                my_HP_current-=100
                            elif random_poke.enemy_skill=="용의분노":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="분출":
                                my_HP_current-=40
                            elif random_poke.enemy_skill=="드래곤다이브":
                                my_HP_current-=120
                            
                            
                            if my_HP_current<=0:
                                my_HP_current=0
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                battle=battle_lose(pokename)
                             
                            else:
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                pygame.display.update()
                            
                        running=True
                        fight=False

                    
                    if skill3_button.getnext(pos):
                        battle_cycle(pokename,pika_skill_list[2])
                        random_poke.HP_current-=60

                        if random_poke.HP_current<=0:
                            random_poke.HP_current=0
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            battle=battle_win(pokename) 
                        else:
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            pygame.display.update()
                            
                            battle_cycle2(random_poke.name,random_poke.random_skill())

                            if random_poke.enemy_skill=="볼트태클":
                                my_HP_current-=70
                            elif random_poke.enemy_skill=="와일드볼트":
                                my_HP_current-=90
                            elif random_poke.enemy_skill=="기합구슬":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="사이코키네시스":
                                my_HP_current-=80
                            elif random_poke.enemy_skill=="플레어드라이브":
                                my_HP_current-=100
                            elif random_poke.enemy_skill=="용의분노":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="분출":
                                my_HP_current-=40
                            elif random_poke.enemy_skill=="드래곤다이브":
                                my_HP_current-=120
                            
                            
                            if my_HP_current<=0:
                                my_HP_current=0
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                battle=battle_lose(pokename)
                             
                            else:
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                pygame.display.update()
                            
                        running=True
                        fight=False


                        
                    if skill4_button.getnext(pos):
                        battle_cycle(pokename,pika_skill_list[3])
                        random_poke.HP_current-=100

                        if random_poke.HP_current<=0:
                            random_poke.HP_current=0
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            battle=battle_win(pokename) 
                        else:
                            random_poke.HP_percent=random_poke.HP_current/random_poke.HP
                            new_width=int(HP_bar.width*random_poke.HP_percent)
                            HP_bar_bg.load()
                            HP_bar.resize(new_width,16,137,100)
                            pygame.display.update()
                            
                            battle_cycle2(random_poke.name,random_poke.random_skill())

                            if random_poke.enemy_skill=="볼트태클":
                                my_HP_current-=70
                            elif random_poke.enemy_skill=="와일드볼트":
                                my_HP_current-=90
                            elif random_poke.enemy_skill=="기합구슬":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="사이코키네시스":
                                my_HP_current-=80
                            elif random_poke.enemy_skill=="플레어드라이브":
                                my_HP_current-=100
                            elif random_poke.enemy_skill=="용의분노":
                                my_HP_current-=60
                            elif random_poke.enemy_skill=="분출":
                                my_HP_current-=40
                            elif random_poke.enemy_skill=="드래곤다이브":
                                my_HP_current-=120
                            
                            
                            if my_HP_current<=0:
                                my_HP_current=0
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                battle=battle_lose(pokename)
                             
                            else:
                                my_HP_percent=my_HP_current/my_HP
                                new_width2=int(HP_bar2.width*my_HP_percent)
                                HP_bar2_bg.load()
                                HP_bar2.resize(new_width2,16,550,263)
                                pygame.display.update()
                        
                        running=True
                        fight=False
                        
                         
                else:
                    button_skill1.load()
                    button_skill2.load()
                    button_skill3.load()
                    button_skill4.load()
                    game.text_ver3(pika_skill_list[0],180,150,0,330)
                    game.text_ver3(pika_skill_list[1],180,150,180,330)
                    game.text_ver3(pika_skill_list[2],180,150,360,330)
                    game.text_ver3(pika_skill_list[3],180,150,540,330)
                    pygame.display.update()
                    game.clock.tick(60)

    forest_img.fade_out_black(480)
    init_screen.load()
    pygame.display.update()
    random_poke.HP_current=random_poke.HP
    HP_bar_bg.load()
    HP_bar.load()
    



def battle_cycle(pokename,skill_name_mypoke):    
    damage_sound=pygame.mixer.Sound("타격음.wav")
    textbar_img.load()
    pygame.display.update()
    time.sleep(0.5)
    game.text_ver2("피카츄의",25,362)
    game.text_ver2(skill_name_mypoke+" 공격",25,410)
    pygame.display.update()
    time.sleep(1)
    damage_sound.play()
    time.sleep(0.5)
    dagame_enemy.load()
    pygame.display.update()
    time.sleep(0.15)
    forest_img.load()
    stage1.load()
    stage2.load()
    interface1.load()
    game.text_ver2(pokename,5,50)
    HP_bar_bg.load()
    HP_bar.load()
    interface2.load()
    game.text_ver2("피카츄",395,215)
    HP_bar2_bg.load()
    HP_bar2.load()
    random_poke_img.load()
    my_poke.load()
    textbar_img.load()
    game.text_ver2("피카츄의",25,362)
    game.text_ver2(skill_name_mypoke+" 공격",25,410)
    pygame.display.update()
    time.sleep(1)



def battle_cycle2(pokename,enemy_skill):
    damage_sound=pygame.mixer.Sound("타격음.wav")
    textbar_img.load()
    pygame.display.update()
    time.sleep(0.5)
    game.text_ver2("상대 "+pokename+"의",25,362)
    game.text_ver2(enemy_skill+" 공격",25,410)
    pygame.display.update()
    time.sleep(1)
    damage_sound.play()
    time.sleep(0.5)
    dagame_mypoke.load()
    pygame.display.update()
    time.sleep(0.15)
    forest_img.load()
    stage1.load()
    stage2.load()
    interface1.load()
    game.text_ver2(pokename,5,50)
    HP_bar_bg.load()
    HP_bar.load()
    interface2.load()
    game.text_ver2("피카츄",395,215)
    HP_bar2_bg.load()
    HP_bar2.load()
    random_poke_img.load()
    my_poke.load()
    textbar_img.load()
    game.text_ver2("상대 "+pokename+"의",25,362)
    game.text_ver2(enemy_skill+" 공격",25,410)
    pygame.display.update()
    time.sleep(1)


    
def battle_win(pokename):
    battle=True
    victory=pygame.mixer.Sound("승리.ogg")
    victory.play()
    victory.set_volume(0.3)
    while battle:
        pygame.display.flip()
        if(random_poke_img.rect.y>330):
            battle=False
        else:
            forest_img.load()
            stage1.load()
            stage2.load()
            interface1.load()
            game.text_ver2(pokename,5,50)
            HP_bar_bg.load()
            HP_bar.load()
            interface2.load()
            game.text_ver2("피카츄",395,215)
            HP_bar2_bg.load()
            HP_bar2.load()
            random_poke_img.moveDown(30)
            random_poke_img.load()
            my_poke.load()
            textbar_img.load()
            pygame.display.update()
            game.clock.tick(60)
    battle_sound.stop()
    game.text("상대 "+pokename+"은/는 쓰러졌다!","")
    game.text(pokename+"와의 전투에서 승리했다!","")
    game.text("피카츄는 소량의 경험치를 얻었다.","")
    victory.stop()
    HP_bar.resize(160,16,137,100)
    HP_bar2.resize(160,16,550,263)
    random_poke_img.moveUp(200)
    return False


def battle_lose(pokename):
    battle=True
    battle_sound.stop()
    while battle:
        pygame.display.flip()
        if(my_poke.rect.y>330):
            battle=False
        else:
            forest_img.load()
            stage1.load()
            stage2.load()
            interface1.load()
            game.text_ver2(pokename,5,50)
            HP_bar_bg.load()
            HP_bar.load()
            interface2.load()
            game.text_ver2("피카츄",395,215)
            HP_bar2_bg.load()
            HP_bar2.load()
            random_poke_img.load()
            my_poke.moveDown(30)
            my_poke.load()
            textbar_img.load()
            pygame.display.update()
            game.clock.tick(60)
    game.text("피카츄은/는 쓰러졌다!","")
    game.text("더이상 싸울 포켓몬이 없다..","눈앞이 깜깜해졌다...")
    HP_bar.resize(160,16,137,100)
    HP_bar2.resize(160,16,550,263)
    my_poke.moveUp(150)
    return False



def game_explain():
    init_screen.load()
    game.display_textbar("오박사인사말")
    textbar_img.load()
    professor_sound=pygame.mixer.Sound("오박사.ogg")
    professor_sound.play(-1)
    professor_sound.set_volume(0.3)

    time.sleep(0.5)
    All_img.fade_in_black(330)
    game.display_textbar("오박사다음말")
    All_img.disappear()
    background_img.load()
    professor_img.load()
    textbar_img.load()

    running=True
    while running:
    
        if(professor_img.rect.x>390):
            running=False
        else:
            professor_img.moveRight(6)
            professor_img.load()
            pygame.display.update()
            game.clock.tick(60)
        
    game.display_textbar("오박사다음말2")
    textbar_img.load()

    poke_ball.load()
    pygame.display.update()
    time.sleep(1)

    running=True
    while running:
        pygame.display.flip() 
        if(poke_ball.rect.y>250):
            running=False
        else:
            y=2
            y+=2*y-1
            x=8
            background_img.load()
            professor_img.load()
            poke_ball.moveDown(y)
            poke_ball.moveLeft(x)
            poke_ball.load()
            pygame.display.update()
            game.clock.tick(60)


    light.resize(20,20,270,250)
    pygame.display.update()
    time.sleep(0.05)

    light.resize(140,140,225,200)
    pygame.display.update()
    time.sleep(0.05)

    light.resize(230,230,195,165)
    pygame.display.update()
    time.sleep(0.15)
    background_img.load()
    professor_img.load()
    pika_poke.load()

    light.resize(140,140,225,200)
    pygame.display.update()
    time.sleep(0.1)
    background_img.load()
    professor_img.load()
    pika_poke.load()

    light.resize(20,20,270,250)
    pygame.display.update()
    time.sleep(0.2)
    background_img.load()
    professor_img.load()
    pika_poke.load()

    pygame.display.update()

    game.display_textbar("오박사다음말3")

    game.display_textbar("오박사다음말4")
    smaller1.fade_in_black(480)
    init_screen.load()
    pygame.display.update()
    
    smaller1.load()
    pygame.display.update()
    time.sleep(1)
    smaller2.load()
    pygame.display.update()
    time.sleep(0.2)
    smaller3.load()
    pygame.display.update()
    time.sleep(0.2)
    smaller4.load()
    pygame.display.update()
    time.sleep(0.2)
    smaller5.load()
    pygame.display.update()

    smaller5.fade_out_black(480)
    init_screen.load()
    pygame.display.update()
    professor_sound.stop()

    
    
    


game=Pokemon_game()

init_screen=Animation("검은색바탕.png",720,480,0,0)
background_img=Animation("오박사배경만.png",720,330,0,0)
All_img=Animation("오박사with배경.png",720,330,0,0)
professor_img=Animation("오박사.png",258,296,225,28)
poke_ball=Animation("몬스터볼.png",60,60,413,141)
light=Animation("빛.png",180,180,210,160)
pika_poke=Animation("피카츄.png",120,150,250,180)
smaller1=Animation("캐릭터 애니메이션(1).png",720,480,0,0)
smaller2=Animation("캐릭터 애니메이션(2).png",720,480,0,0)
smaller3=Animation("캐릭터 애니메이션(3).png",720,480,0,0)
smaller4=Animation("캐릭터 애니메이션(4).png",720,480,0,0)
smaller5=Animation("캐릭터 애니메이션(5).png",720,480,0,0)
forest_img=Animation("배틀 배경(수풀).png",720,330,0,0)
dagame_enemy=Animation("데미지이펙트.png",150,150,475,65)
dagame_mypoke=Animation("데미지이펙트.png",150,150,125,165)
HP_bar=Animation("HP.png",160,16,137,100)
HP_bar_bg=Animation("하얀색바탕.png",160,16,137,100)
interface1=Animation("인터페이스1.png",350,130,0,18)
HP_bar2=Animation("HP.png",160,16,550,263)
HP_bar2_bg=Animation("하얀색바탕.png",160,16,550,263)
interface2=Animation("인터페이스2.png",385,125,335,190)
battle_sound=pygame.mixer.Sound("야생포켓몬.ogg")



game.start_gamescreen() 
game_explain()


screen = pygame.display.set_mode((720,480))
game1 = Game(screen)
game1.set_up()


position_x_list=[60,90,120,150,180,210,240,270,300]
position_y_list=[60,90,120,150]
random_x=random.choice(position_x_list)
random_y=random.choice(position_y_list)
position_x_list1=[90,120,150,180]
position_y_list1=[210,240,270]
random_x1=random.choice(position_x_list1)
random_y1=random.choice(position_y_list1)
position_x_list2=[240,270,300,330,360]
position_y_list2=[300,330,360]
random_x2=random.choice(position_x_list2)
random_y2=random.choice(position_y_list2)

while game1.game_state == GameState.playing:
    game1.update()
    pygame.display.update()
    game.clock.tick(60)

    if game1.player.rect.x==random_x and game1.player.rect.y==random_y:
        grass_img=Animation("수풀.png",1440,200,50,150)
        stage1=Animation("발판.png",335,80,-360,135)
        stage2=Animation("발판.png",430,120,720,280)
        player_img_battle=Animation("캐릭터.png",200,200,850,130)
        my_poke=Animation("피카츄(뒷모습).png",200,200,75,155)
        battle()
        random_x=random.choice(position_x_list)
        random_y=random.choice(position_y_list)
    elif game1.player.rect.x==random_x1 and game1.player.rect.y==random_y1:
        grass_img=Animation("수풀.png",1440,200,50,150)
        stage1=Animation("발판.png",335,80,-360,135)
        stage2=Animation("발판.png",430,120,720,280)
        player_img_battle=Animation("캐릭터.png",200,200,850,130)
        my_poke=Animation("피카츄(뒷모습).png",200,200,75,155)
        battle()
        random_x1=random.choice(position_x_list1)
        random_y1=random.choice(position_y_list1)
    elif game1.player.rect.x==random_x2 and game1.player.rect.y==random_y2:
        random_x2=0
        random_y2=0
        grass_img=Animation("수풀.png",1440,200,50,150)
        stage1=Animation("발판.png",335,80,-360,135)
        stage2=Animation("발판.png",430,120,720,280)
        player_img_battle=Animation("캐릭터.png",200,200,850,130)
        my_poke=Animation("피카츄(뒷모습).png",200,200,75,155)
        battle()
        random_x2=random.choice(position_x_list2)
        random_y2=random.choice(position_y_list2)
