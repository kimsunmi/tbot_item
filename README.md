# 디스코드 봇 메뉴얼_김선미 산출물

## 📒 과제 개요

 알고리즘의 경우 수학 문제 풀듯이 꾸준히 문제들을 풀어야 실력이 늘어납니다. 하지만 알고리즘을 처음 공부할 때의 저는 지속적으로 문제를 푼다는 건 어렵다고 느꼈습니다. 문제 유형을 처음 접할 뿐 더러 한 문제에 꽤 오랜 시간 투자하여 성취감을 느끼기보단 겨우 풀었다는 감정 소비가 더 컸기 때문입니다. 이런 고질적 문제를 방지하고자 게임형식으로 알고리즘을 다뤄보자는 알고알고 프로젝트에 참여하게 되었습니다.

## 🗒️ 작품 구성 및 상세 내용

 디스코드 봇을 기반으로 사람들에게 친숙한 보드게임으로 알고리즘 게임을 제작했습니다. 단순히 문제를 풀고 앞으로 나아가는게 아니라 상대방과의 경쟁과 보드게임 판에서 일어날 수 있는 함정/보상으로 관심을 끌어 일시적이 아닌 지속적으로 알고리즘에 흥미를 가졌으면 하는 바람입니다.

✔️ **알고알고 - 아이템 @**

<aside>
🔎 **아이템 사용 !useitem**
사용자가 갖고 있는 아이템 목록을 출력 후 
일정 시간 내에 아이템을 입력받아 사용합니다.  

**구현** **아이템 목록**
**REDEMPTION:** 문제 풀지 않고 STEP 사용 가능하도록 status 1로 변경
**ASSASSIN:** 상대 사용자 위치에서 뒤로 한 칸 이동
**STUN:** 상대 사용자가 하루동안 STEP 사용 못하게 하기
*구현 예정
BOMB, CAFFEINE 등

*다른 팀원(algoalgo_map)이 구현
~~STEP~~: ~~한칸 앞으로 이동~~
~~SNAKE~~: ~~STEP을 하다 뱀을 만날시 내려간 것을 방지~~

**아이템 사용 형식**
1) !useitem 입력
2) 사용할 아이템 번호 입력
이때, assassin, stun의 경우 아이템 번호 및 유저 이름
예시: 1 steven

</aside>

        

## 📝 개발 세부 내용 및 구현 결과

- algoalgo_item.py - 내부 함수
    
    <aside>
    📢 아이템과 관련된 함수를 포함하고 있습니다.
    (ex: 아이템 목록💊💣🍺 출력, 아이템 사용 및 상태 업데이트, 등)
    
    </aside>
    
    **함수명(인자)**
    
    - checkMember(사용자)
        
        <aside>
        ⚙️ checkMember 함수를 호출 시 
        요청된 사용자가 DB에 존재하는지 확인 후 결과 return
        
        </aside>
        

        
    - setStun(사용자)
        
        <aside>
        ⚙️  setStun 함수를 호출 시 
        해당 사용자의 stat을 -1로 변경하여 DB에 업데이트
        
        </aside>
        

        
    - setRedemption(사용자)
        
        <aside>
        ⚙️ setRedemption 함수를 호출 시 
        해당 사용자의 stat을 1로 변경하여 DB에 업데이트
        
        </aside>
        

        
    - updateitem(사용자, 아이템)
        
        <aside>
        ⚙️ updateitem 함수를 호출 시 
        1) 해당 사용자가 DB에 있는지 확인 후 사용자의 아이템 목록 return 받기
        2) return 된 아이템 목록에서 사용된 아이템을 1개 지운 후 DB에 업데이트
        
        </aside>

        
    - setAssassin(사용자)
        
        <aside>
        ⚙️ setAssassin 함수를 호출 시
        1) 해당 사용자가 DB에 있는지 확인 후 사용자의 위치 return 받기
        2) return 된 위치 값에서 -1한 값을 DB에 업데이트
        
        </aside>
        

        
    - useitem(사용자)
        
        <aside>
        ⚙️ useitem 함수를 호출 시
        1) 해당 사용자가 DB에 있는지 확인 후 아이템 목록 return 받기
        1-1) show_items를 호출하여 아이템 목록 정리 → 팀장님의 도움
        2) 아이템을 갖고 있는지 보유 현황 return (이때, 없을 경우 0)
        
        </aside>
        

        
        - show_items(아이템 목록)
            
            <aside>
            ⚙️ show_items 함수를 호출 시 
            ** useitem (1)에서 return 받은 아이템 목록을 인자값으로 사용한다 **
            아이템 목록을 아래 dictionary 형식으로 정리하여 return
            
            </aside>
            

            
- algoalgo_main.py - item 코드 및 실행 결과
    - 실행 결과 💡
        
        ✏️ **!useitem 명령어 실행 결과**
        

    
    <aside>
    1️⃣ 디스코드 봇이 가동중일때 사용자가 !useitem 입력 시 
    1) 사용자의 이름을 기반으로 algoalgo_item의 useitem 함수 호출
    1-1) 아이템 보유 현황을 return 받는다
    2) 아이템 목록을 출력 후 사용하고자 할 아이템 번호를 입력받기를 10초동안 대기
    
    </aside>

    
    - 실행 결과 💡
        
        ✏️ **!useitem 명령어 실행 후 응답을 안한 경우**
        
        ![시간 내 응답을 안한 경우](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c2a6c35b-ffa1-4e73-b231-9b02b282b0ff/Untitled.png)
        
        시간 내 응답을 안한 경우
        
        ![입력값이 올바르지 않은 경우](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21828f21-781a-4d5e-9b49-109e157851f0/Untitled.png)
        
        입력값이 올바르지 않은 경우
        
    
    <aside>
    2️⃣ 3-1) 시간동안 입력이 없을 경우 return 
    3-2) 사용자의 입력값 중 사용자와 번호가 올바른지 검사
    ① 입력값이 제대로된 형식으로 들어왔는가?
    ② 인덱스가 유효범위내에 있는가?
    ③ 사용자의 id가 DB에 있는가? → algoalgo_item의 checkMember 함수 호출
    
    </aside>
    


    
    - 실행 결과 💡
        
        ✏️ **아이템 입력 받은 결과 예시**
        
        
    
    <aside>
    3️⃣ 4) 사용자의 입력값의 아이템 명을 기반으로 다중 if문 구분
    4-1) 입력값이 STUN이고 길이가 2인 경우 (=다른 유저에게 사용하는 경우)
    ① algoalgo_item의 setStun 호출하여 상대방의 status 업데이트
    ② algoalgo_item의 updateitem 호출하여 STUN;을 아이템 목록에서 삭제하여 업데이트
    4-2) 입력값이 REDEMPTION인 경우
    ① algoalgo_item의 setRedemption 호출하여 상태 status 업데이트
    ② algoalgo_item의 updateitem 호출하여 REDEMPTION;을 아이템 목록에서 삭제하여 업데이트
    4-3) 입력값이 ASSASSIN인 경우
    ① algoalgo_item의 setASSASSIN 호출하여 상태 status 업데이트
    ② algoalgo_item의  updateitem 호출하여 ASSASSIN;을 아이템 목록에서 삭제하여 업데이트
    
    </aside>

    
    <aside>
    4️⃣ 4-4) 입력값이 STEP인 경우
    *map과 연계되는 부분입니다.*
    
    </aside>
    

## ⭐ 기대 효과

1. 지속적인 참여 유도 가능
2. 일부 운영에 있어 자동화로 인한 시간 절약 가능
