
import smtplib, ssl
from email.mime.text import MIMEText
import myGmailAccount as gmail #지메일 계정 모듈
import sendGmail

html = """
<div role="article" lang="en" style="padding:20px 0px;margin:0 auto;background:#ffffff"><div style="height:0px;max-height:0px;border-width:0px;border:0px;border-color:initial;line-height:0px;font-size:0px;overflow:hidden;display:none"></div><table id="m_-5989121191543860408$beacon$"><tbody><tr><td></td></tr></tbody></table><img src="https://ci3.googleusercontent.com/meips/ADKq_NZqlcW1rmg22_fMBtrBdHAkuR5T6HDUjQjsvgyg48C_ccon64NPNebwvfcxw4o-FncKU6_QKwcNBd4OlSjRaZUuRse2-O7065QDcdIE0bmr0BTsCCc=s0-d-e1-ft#https://event.stibee.com/v2/open/MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw" width="0" height="0" style="height:0px;max-height:0px;border-width:0px;border-color:initial;line-height:0px;font-size:0px;overflow:hidden" class="CToWUd" data-bit="iit"><table id="m_-5989121191543860408stb-container" role="presentation" style="width:100%;background:#ffffff" border="0"><tbody><tr><td align="center"><div style="width:100%;max-width:630px;background:#ffffff;margin:0px auto"><table width="100%" cellpadding="0" cellspacing="0" style="border:0"><tbody><tr><td style="padding:0 0;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:12px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#747579"><table border="0" cellpadding="0" cellspacing="0" style="width:100%"><tbody><tr><td style="padding:15px 15px 15px 15px"><div><span style="color:#747579;font-size:12px;text-decoration:none"><a href="https://event.stibee.com/v2/click/MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw/aHR0cHM6Ly9zdGliLmVlL3RENjk" style="text-decoration:inherit;color:#747579" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://event.stibee.com/v2/click/MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw/aHR0cHM6Ly9zdGliLmVlL3RENjk&amp;source=gmail&amp;ust=1706157213762000&amp;usg=AOvVaw3f3qf6fss-OBmeo_9djiy4">이 메일이 잘 안보이시나요?</a></span></div></td></tr></tbody></table></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>안녕하세요! 뤼튼 팀 입니다.&nbsp;</div><div><br></div><div>뤼튼과의 채팅 그리고 스토어에 있는 다양한 툴 사용은 어떠셨나요? 마음에 드셨나요? 사실 뤼튼을 제대로 활용하기 위해서는 뤼튼에게 잘 질문해야 해요. 이것을 저희는 프롬프트라고 말해요. 그러면 프롬프트를 통해 200%이상 만족스러운 답변을 받는 비결! 지금부터 알려드릴께요!</div></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="border:0"><tbody><tr><td style="height:15px" colspan="3"></td></tr><tr><td style="width:15px"></td><td style="height:15px;background:none;padding:0px;border-top-width:1px;border-top-style:solid;border-top-color:#999999;margin:0 0"></td><td style="width:15px"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div><span style="font-size:20px;font-weight:bold">1<span>. 더 정확한 컨텍스트를 제공하면 더 좋은 답변을 얻을 수 있어요.</span></span></div><div><br></div><div><p>“뤼튼은 똘똘한 신입사원!<span style="font-style:italic">”</span></p><p><br></p><p>좋은 답변을 얻기 위해서는 좋은 질문이 필요해요. 여기서 말하는 좋은 질문이란 충분한 컨텍스트(맥락)가 포함된 질문을 의미하죠. 그래서 뤼튼을 이해하는 가장 좋은 방법은 똘똘한 신입사원으로 생각하는 것이랍니다.</p><p><br></p><p>어떤 신입사원이든 어떤 회사에 처음 입사하면 적응하는데 시간이 필요하죠. 우리 회사 분위기는 어떤지, 누가 의사결정 권한을 가지고 있는지 등등 아직 파악되지 않은 상황들이 많기 때문입니다. 그러나 이 신입사원 옆에 조금 친절한 사수가 있다면 빠르게 회사에 적응할 수 있을거예요. 바로 그 친절한 사수가 여러분입니다.</p><p><br></p><p>예를 들어볼까요? 이 뤼튼 신입사원이 영어를 무척이나 잘한다고 들었어요. 그래서 한글 문장을 주면서 영어로 번역해 달라고 요청했더니 다음과 같이 답변해주었습니다.</p></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:15px 15px 0px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_Nbhzwgkb-U7dsDHUDenvn1XmmUJS3n6FNuo-KiH67KVpp4UGQm_d2uAb_WbqXuLbkijffSau_pUDktvBn4S6EFd=s0-d-e1-ft#https://img.stibee.com/68527_1695638190.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 964.719px;"><div id=":qh" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT" data-tooltip="Download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:5px 15px 15px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NZKbltomDe7qBIwT_HFs4tm6-Hg_8ZCfJ6AegcvRaNEt-fheicHmLGHy_wia8sdUXm6AvaQXfgZM75MWKyZx-0r=s0-d-e1-ft#https://img.stibee.com/68527_1695638198.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 1188.68px;"><div id=":qj" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT" data-tooltip="Download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>자 이번에는 번역을 하는 이유와 함께 조금 자세하게 질문을 던져봤어요.</div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:15px 15px 0px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NaxVRFPOYt33GmiCMXEUYdDP9Trfz4APv1iTInCC9hV4L2Sv0CcBlXnOZH7KyffkLc0Lq8Yg2bboGEZDr97UO9r=s0-d-e1-ft#https://img.stibee.com/68527_1695638229.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 1508.73px;"><div id=":qk" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT" data-tooltip="Download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:5px 15px 15px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NZVMY1fftyYiupaEaU6swij6ggNqcK45-VaC35XyLXexgWiBmiD4Hm-44V1-2egkXcsKpAl1gXwIX_Vr3aF9WC7=s0-d-e1-ft#https://img.stibee.com/68527_1695638232.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 2002.94px;"><div id=":ql" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT" data-tooltip="Download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>이번엔 완전히 업그레이드된 답변을 받게 되었죠. 이 문장을 왜 영어로 번역해야 하는지를 보다 자세하게 설명해주었더니 일을 훨씬 잘하는 것을 알 수 있습니다. 그래서 우리는 인공지능에게 일을 시킬 때 아직 우리회사 사정을 모르는 신입사원에게 알려주듯 명확한 컨텍스트를 제공해야 해요.&nbsp;</div><div><br></div><div>이와 더불어 #정확한 목표 #하나의 문장에는 하나의 포인트 #정확한 동사 #올바른 맞춤법을 사용한다면 더 멋진 결과물을 얻으실 수 있을거예요.</div></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="border:0"><tbody><tr><td style="height:15px" colspan="3"></td></tr><tr><td style="width:15px"></td><td style="height:15px;background:none;padding:0px;border-top-width:1px;border-top-style:solid;border-top-color:#999999;margin:0 0"></td><td style="width:15px"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div><span style="font-size:20px;font-weight:bold"><span>2. 인공지능은 분석을 능숙하게 해요.</span></span></div><div><p><br></p><p>인공지능은 분석을 참 잘해요. 예를 들어볼까요? 아래는 Google Sheet에 있는 표를 복사해서 붙여넣은 뒤 점수가 높은 순으로 테이블로 정리해달라고 요청해보았어요. 이렇게 주어진 정보를 분석하고, 요약하는 일이 생성형 AI의 가장 큰 장점 중 하나입니다. 이 경우 거짓말이나 환각 현상을 크게 줄일 수 있다는 것도 장점이죠.</p></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:0px 15px 0px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NbLueG2uePPn3sFoMO9DsDNrFrLI9a7USDrcVIm7duz9T070A6kIwqwd8l8AFaxphnoQNEazcBc7sTKDMVTYD6c=s0-d-e1-ft#https://img.stibee.com/68527_1695638319.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 2688.46px;"><div id=":qm" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" title="Download" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:0px 15px 15px 15px"><p>&nbsp;<span style="font-style:italic">엑셀 또는 구글 스프레드시트 내용을 복사&amp;붙여넣기 후 분석 및 정리도 가능하다</span></p></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="border:0"><tbody><tr><td style="height:15px" colspan="3"></td></tr><tr><td style="width:15px"></td><td style="height:15px;background:none;padding:0px;border-top-width:1px;border-top-style:solid;border-top-color:#999999;margin:0 0"></td><td style="width:15px"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div><span style="font-size:20px;font-weight:bold"><span>3. 적절한 예시를 주면 더 원하는 답변을 얻을 수 있어요.</span></span></div><div><p><br></p><p>예시를 잘 주면 패턴을 학습시킬 수 있어요. 우리가 신입사원에게 일을 시킬 때 여러번 업무지시를 시키는것 보다도 좋은 방법이 있는데요. 바로 관련 예시나 레퍼런스를 제공하는 것입니다. 그러면 요청하는 사람의 의도를 보다 명확하게 파악할 수 있게 될 거예요. 인공지능 역시 마찬가지입니다. 인공지능에게도 적절한 예시를 주면 더 적절한 답변을 만들어줍니다.</p><p><br></p><p>예를 들어 아래와 같이 "장희빈"이라는 단어를 이용하여 초성 개그를 만들어달라고 요청해봤어요.</p></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:15px 15px 0px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NZYkF1XPHi1vYoCQ6yo8av4YtOvnpPwEpBA0MHqmp5TWzH2FE6A0F7Pozk3URID9dJj7pX53DArI2WcIOJNmwL4=s0-d-e1-ft#https://img.stibee.com/68527_1695638449.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd" data-bit="iit"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:5px 15px 15px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NbcS79Tdslmq8uZpECaJqHrQa052-ktJiTDXT5OG563KIjML_p9YRN1dymxz6qMHxPH37uCJd2Q5L4uTO9UT9kW=s0-d-e1-ft#https://img.stibee.com/68527_1695638456.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd" data-bit="iit"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>그런데 안타깝게도 초성개그가 무엇인지 못알아들은것 같아요. 그래서 아래와 같이 초성개그 예시를 함께 던져주었어요.</div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:15px 15px 0px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_NadsKEc86p2lr-AAsRLl0cONUz8yAFVLm1PnbqulBDUYMiN3VVAYm4ttRM-b4HVcuzIAL6xIVxMzy3TYft55ZOf=s0-d-e1-ft#https://img.stibee.com/68527_1695638504.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd a6T" data-bit="iit" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 769.667px; top: 3483.82px;"><div id=":qi" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTc4NzY2MDcyODA0NTQwODY4NiJd; 43:WyJpbWFnZS9qcGVnIl0." data-tooltip-class="a1V" jsaction="JIbuQc:.CLIENT" data-tooltip="Download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="text-align:justify;font-size:0;box-sizing:border-box;padding:5px 15px 15px 15px"><img src="https://ci3.googleusercontent.com/meips/ADKq_Nb-dyncMNL7JRIcwnQHW42VOs-Q7ms2jP7qM6TEYYc8_WxsZP6kx09ugwcuyIbTWJ48Can08-ILxbVssL7hCQeO=s0-d-e1-ft#https://img.stibee.com/68527_1695638511.png" alt="" style="display:inline;vertical-align:bottom;text-align:justify;max-width:100%!important;height:auto;border:0" width="600" class="m_-5989121191543860408stb-justify CToWUd" data-bit="iit"></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>위와 같이 제가 원하는 예시를 전달했더니 답변도 그에 맞게 정리해주네요! 신기하죠? 이렇게 적절한 예시를 제공하면 그 예시를 바탕으로 다음 질문을 만들어냅니다. 이를 Few-shot Paradigm 또는 In-context Learning 이라고 말하는데요. 앞서서 설명한 충분한 컨택스트를 주는것과 비슷한 맥락이기도 합니다. 즉, 더 적절한 예시를 통해 더 그에 맞는 결과를 도출하는 것이죠. 어찌보면 인간이 학습하는 방식과 정말 비슷하지 않나요?</div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div><span style="font-size:20px;font-weight:bold"><span>우리 회사의 '똑똑한' '신입'사원!</span></span></div><div><ul style="padding:0;margin:0 0 0 30px"><li>뤼튼 <span style="font-weight:bold">= 굉장히 똑똑하지만 친절한 사수가 필요한 얼떨떨 신입사원</span></li></ul><p>이제부터 인공지능의 똘똘함을 100%, 200% 끌어내는 힘은 인공지능의 '사수', 바로 여러분에게 달렸습니다! 인공지능의 훌륭한 사수가 되어 부사수(Co-pilot) 뤼튼의 역량을&nbsp; 최대로 발휘해 보세요!</p></div></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td width="100%" style="clear:both"><table border="0" cellpadding="0" cellspacing="0" style="width:100%"><tbody><tr><td style="padding:15px 15px 25px 15px;border:0;width:100%;text-align:center"><table border="0" cellpadding="0" cellspacing="0" style="color:#ffffff;background:#ff5252;border-radius:3px;box-sizing:border-box;text-decoration:none;outline:0px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif;text-align:center;display:inline-table"><tbody><tr><td style="font-size:0;background:none;border-radius:3px;padding:19px 20px;text-align:center" valign="top"><a href="https://event.stibee.com/v2/click/MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw/aHR0cHM6Ly9haXJicmlkZ2Uud3J0bi5haS93N2RiNWw" style="font-size:16px;display:inline-block;color:#ffffff;text-decoration:none;outline:0px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif;text-align:center;line-height:1;box-sizing:border-box" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://event.stibee.com/v2/click/MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw/aHR0cHM6Ly9haXJicmlkZ2Uud3J0bi5haS93N2RiNWw&amp;source=gmail&amp;ust=1706157213763000&amp;usg=AOvVaw05mkYPOBwaeR05wdZQQFo0">지금 경험하기</a></td></tr></tbody></table><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"><tbody><tr></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><table role="presentation" class="m_-5989121191543860408stb-one-col" style="width:100%;border:0" cellpadding="0" cellspacing="0"><tbody><tr><td style="word-break:break-all;text-align:left;margin:0px;line-height:1.7;word-break:break-word;font-size:16px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#000000;padding:15px 15px 15px 15px"><div>&nbsp; &nbsp;</div><div><br></div></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="border:0"><tbody><tr><td style="text-align:center;margin:0px;line-height:1.7;word-break:break-word;font-size:12px;font-family:noto sans kr,noto sans cjk kr,noto sans cjk,Malgun Gothic,apple sd gothic neo,nanum gothic,malgun gothic,dotum,arial,helvetica,Meiryo,MS Gothic,sans-serif!important;color:#747579;border:0"><table border="0" cellpadding="0" cellspacing="0" style="width:100%"><tbody><tr><td style="padding:15px 15px 15px 15px;text-align:center"><div><span style="color:#747579;font-size:12px">주식회사 뤼튼테크놀로지스</span><br><span style="color:#747579;font-size:12px"><a href="mailto:contact@wrtn.io" target="_blank">contact@wrtn.io</a></span><br><span style="color:#747579;font-size:12px">서울 강남구 테헤란로2길 27, 1503호 02-499-1885</span><br><a href="https://page.stibee.com/unsubscribe/281107?token=MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw" style="text-decoration:underline;color:#606060;font-size:12px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://page.stibee.com/unsubscribe/281107?token%3DMjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw&amp;source=gmail&amp;ust=1706157213763000&amp;usg=AOvVaw1BlpWEc-dw5m_nFWhlpyxU">수신거부</a>&nbsp;<a href="https://page.stibee.com/unsubscribe/281107?token=MjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw" style="text-decoration:underline;color:#606060;font-size:12px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://page.stibee.com/unsubscribe/281107?token%3DMjgxMTA3LzE3ODExMDIvOTU2Nzc3Lw&amp;source=gmail&amp;ust=1706157213763000&amp;usg=AOvVaw1BlpWEc-dw5m_nFWhlpyxU">Unsubscribe</a></div></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table><div style="padding:10pt 0cm 10pt 0cm"><p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US"></span></p></div></div>
"""

msg = sendGmail.make_mime_text(
    mail_to = gmail.account,
    subject = "HTML",
    body = html
)

sendGmail.send_gmail(msg)
print("HTML email 전송 완료")