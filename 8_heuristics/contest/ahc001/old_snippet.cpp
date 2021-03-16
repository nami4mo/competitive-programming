            // shrink_kaizen=0;
            // shrink=true;
            // Ad &ad = state.ads[adi];

            // // shrink_dir=rand_dir4(mt64);

            // double xyratio = (1.0)*(ad.x1-ad.x0)/((ad.x1-ad.x0)+(ad.y1-ad.y0));
            // if(rand_01(mt64)<xyratio) shrink_dir=0;
            // else shrink_dir=2;
            // shrink_dir+=rand_dir4(mt64)%2;

            // int shrink_dist_max;
            // if(shrink_dir==0)      shrink_dist_max=ad.tx-ad.x0;
            // else if(shrink_dir==1) shrink_dist_max=ad.x1-ad.tx-1;
            // else if(shrink_dir==2) shrink_dist_max=ad.ty-ad.y0;
            // else if(shrink_dir==3) shrink_dist_max=ad.y1-ad.ty-1;
            
            // // dist_max を 0〜500 で適当に選んだ方が精度良かった...
            // shrink_dist_max=2*shrink_dist_max/5;
            // if(shrink_dist_max<=0) continue;
            // int shrink_dist=1+rand_hw(mt64)%shrink_dist_max;
            // // if(shrink_dist<shrink_dist_max/3) shrink_dist+=shrink_dist_max/3;
            // shrink_kaizen=shrink_ad(state,adi,shrink_dir,shrink_dist);
            // if(shrink_kaizen==0ll) shrink=false;

            // int need_dist;
            // if(shrink_dir<=1) need_dist=shrink_dist*(ad.y1-ad.y0)/(ad.x1-ad.x0);
            // else need_dist=shrink_dist*(ad.x1-ad.x0)/(ad.y1-ad.y0);

            // dir=rand_dir4(mt64);
            // if(shrink_dir<=1) dir=2+dir%2;
            // else dir=dir%2;
            // ret = try_to_expand_large(state, adi, dir, need_dist+1 );
            // if(!ret && shrink){
            //     try_to_expand_large(state, adi, shrink_dir, shrink_dist); // shrinkを戻す
            // }


    //// 最後のused と ads の状態を比較してみる
    // for(int i=0;i<n;i++){
    //     Ad &ad=state.ads[i];
    //     for(int x=ad.x0;x<ad.x1;x++){
    //         for(int y=ad.y0;y<ad.y1;y++){
    //             if(state.used[x][y]!=i){
    //                 DEBUG(i);
    //             }
    //             state.used[x][y]=n+1;
    //         }
    //     }
    // }
    // int wa=0;
    // int wa_hamidasi=0;
    // for(int x=0;x<HW;x++){
    //     for(int y=0;y<HW;y++){
    //         if(state.used[x][y]!=-1 && state.used[x][y]!=n+1){
    //             // DEBUG(x);
    //             // DEBUG(y);
    //             if(state.used[x][y]<n+1) wa_hamidasi++;
    //             wa+=1;
    //         }
    //     }
    // }
    // DEBUG(wa);
    // DEBUG(wa_hamidasi);


    // WA逃れの苦肉の策...
    // for(int i=0;i<n;i++){
    //     for(int j=i+1;j<n;j++){
    //         Ad &ad_a=state.ads[i];
    //         Ad &ad_b=state.ads[j];
    //         if( check_overlap(ad_a.x0,ad_a.x1, ad_b.x0,ad_b.x1) && check_overlap(ad_a.y0,ad_a.y1, ad_b.y0,ad_b.y1)){
    //             if(ad_b.x0<ad_a.x1){
    //                 ad_a.x1=ad_b.x0;
    //             }
    //             else{
    //                 ad_a.x0=ad_b.x1;
    //             }
    //         }
    //         if(ad_a.x0<0) ad_a.x0=0;
    //         if(ad_a.x1>HW) ad_a.x1=HW;
    //         if(ad_a.y0<0) ad_a.y0=0;
    //         if(ad_a.y1>HW) ad_a.y1=HW;
    //     }
    //     //TODO: 完全に消えてた時の処理（適当にどっかの空きマスに埋める？）
    // }