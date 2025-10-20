import matplotlib.pyplot as plt
import seaborn as sns
from lib.setting import *

def create_boxplot_(df,title,items,labels,fname,order=None,hue=None,color="Blues_d",degree=0,xsize=16,ysize=5,mean_line=True,zero_line=False,annot=False):
    fig = plt.figure(figsize=(xsize,ysize))
    plt.subplots_adjust(wspace=0.1,hspace=0.3)
    
    for i in range(len(items)):
        
        color = check_color(items[i],color)
        
        ax = fig.add_subplot(1,len(items),i+1)
        df_ = df.dropna(subset=[items[i]])
        sns.boxplot(x=labels,y=items[i],data=df_,palette=color,order=order,hue=hue,ax=ax)
        plt.xticks(rotation=90,fontsize=8)
        plt.yticks(fontsize=8)
        
        if i != 0 and items[i] not in av:
            ax.set_yticklabels("")
            
        if items[i] in bn:
            plt.title(items[i][:3],fontsize=8)
            plt.xlabel(items[i][4:],fontsize=8,rotation=degree)
            plt.ylim(-2,2)
        else:
            plt.xlabel(items[i].replace("_gap","").replace("_growth",""),rotation=degree)
            
        if items[i] in tre:
            plt.ylim(-2,2)
        
        if items[i] in (cn+cat+cn_self):
            plt.ylim(-0.05,1.05)
        
        if items[i] in (cn_gp):
            plt.ylim(-0.6,0.6)
            
        if items[i] in (cn_gap):
            plt.ylim(-0.85,0.85)
            
        if items[i] in av:
            plt.ylim(None,None)
            plt.yticks(fontsize=6)
        
        if mean_line == True:
            mean = df_[items[i]].mean()
            x_min, x_max = ax.get_xlim()
            plt.hlines(mean,x_min,x_max,linestyles=":",colors="r")
            if annot == True:
                plt.annotate("全社平均",(x_max,mean),fontsize=5)
            
        if zero_line == True:
            plt.hlines(0,-0.5,len(df[labels].unique())-0.5,linestyles="--",colors="r")
            
        plt.ylabel("")
    plt.suptitle(title)
    plt.savefig(fname,dpi=200,pad_inches=0.2,bbox_inches="tight")

def check_color(item,base_color):
    item = item.replace("_self","")
    if item in ['課題設定', '解決意向','論理的思考', '疑う力', '創造性']:
        return "Wistia_r"
    elif item in [ '個人的実行力', '内的価値', 'ヴィジョン', '自己効力', '成長', '決断力', '耐性', '感情コントロール', '興味']:
        return "Reds_d"
    elif item in ['表現力', '柔軟性', '共感・傾聴力', '寛容', '外交性', '影響力の行使', '情熱・宣教力']:
        return "Greens_d"
    elif item in ['組織への働きかけ', '地球市民', '組織へのコミットメント', '誠実さ']:
        return "Blues_d"
    else:
        return base_color
    
def create_scatterplot(df,target_df,xcol,ycol,*rels,fname,
                       xdesc="",ydesc="",title=None,xmax=None,xmin=None,ymax=None,ymin=None):

    fig, ax = plt.subplots(
        2, 2, # 縦 x 横
        gridspec_kw=dict(width_ratios=[6,1], height_ratios=[1,6], wspace=0.01, hspace=0.01), # 今回のミソ
        sharex='col', sharey='row', figsize=(8,8) # もちろん他の引数と併用可
    )

    ax1 = ax[0][0]
    ax2 = ax[1][0]
    ax3 = ax[1][1]

    # ビッグデータのプロット
    sns.distplot(df[xcol],ax=ax1)
    sns.scatterplot(x=xcol,y=ycol,data=df,ax=ax2,alpha=0.05)
    sns.distplot(df[ycol],ax=ax3,vertical=True)

    ax1.set_yticklabels("")
    ax1.set_ylabel("")
    ax1.set_xlim(xmin,xmax)
    ax3.set_xticklabels("")
    ax3.set_ylabel("")
    ax3.set_ylim(ymin,ymax)

    # 対象者のプロット
    for rel in rels:
        buf = target_df.query("RELATION=='{}'".format(rel))
        sns.distplot(buf[xcol],ax=ax1,label=rel,color=rel_cols[rel])
        sns.distplot(buf[ycol],ax=ax3,vertical=True,color=rel_cols[rel])
    sns.scatterplot(x=xcol,y=ycol,data=target_df,alpha=0.1,
                    hue="RELATION",hue_order=rels,ax=ax2,
                    palette=colors,linewidth=0)
    
    # ラベル名
    ax2.set_ylabel(ycol+"\n"+ydesc)
    ax2.set_xlabel(xcol+"\n"+xdesc)
    ax2.set_xlim(xmin,xmax)
    ax2.set_ylim(ymin,ymax)
    
    ax1.set_title(title,fontsize=16)
    
    plt.savefig(fname,dpi=200,pad_inches=0.2,bbox_inches="tight")