# 47都道府県別人口データ（2024年10月1日現在）
# データソース: 総務省統計局人口推計データ
# japan.geojsonのnam_jaフィールドと対応する形式

# 都道府県別人口データフレーム作成
japan_population_2024 <- data.frame(
  prefecture = c(
    "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
    "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
    "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
    "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
    "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
    "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
    "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"
  ),
  population = c(
    5041491, 1164710, 1144407, 2247139, 896324, 1010776, 1742317,
    2810049, 1882342, 1889425, 7329258, 6275423, 14192184, 9223695,
    2098804, 995955, 1098531, 738691, 790215, 1988462, 1913076,
    3524160, 7465250, 1711370, 1400812, 2521262, 8770315, 5336665,
    1285094, 879617, 531085, 641396, 1830621, 2716733, 1279601,
    685357, 917058, 1275349, 655698, 5097710, 787675, 1250705,
    1696144, 1085198, 1031344, 1530203, 1467065
  ),
  population_thousands = c(
    5041.491, 1164.710, 1144.407, 2247.139, 896.324, 1010.776, 1742.317,
    2810.049, 1882.342, 1889.425, 7329.258, 6275.423, 14192.184, 9223.695,
    2098.804, 995.955, 1098.531, 738.691, 790.215, 1988.462, 1913.076,
    3524.160, 7465.250, 1711.370, 1400.812, 2521.262, 8770.315, 5336.665,
    1285.094, 879.617, 531.085, 641.396, 1830.621, 2716.733, 1279.601,
    685.357, 917.058, 1275.349, 655.698, 5097.710, 787.675, 1250.705,
    1696.144, 1085.198, 1031.344, 1530.203, 1467.065
  ),
  stringsAsFactors = FALSE
)

# データの確認
print(paste("データ数:", nrow(japan_population_2024)))
print("人口上位5都道府県:")
print(head(japan_population_2024[order(japan_population_2024$population, decreasing = TRUE), ], 5))

# japan.geojsonのnam_jaフィールドとの対応確認用
# geojsonファイルを読み込む場合の例（rgdalまたはsfパッケージが必要）
# library(sf)
# geojson_data <- st_read("japan.geojson")
# geojson_prefectures <- unique(geojson_data$nam_ja)
# 
# # 都道府県名の対応確認
# missing_in_population <- setdiff(geojson_prefectures, japan_population_2024$prefecture)
# missing_in_geojson <- setdiff(japan_population_2024$prefecture, geojson_prefectures)
# 
# if(length(missing_in_population) == 0 && length(missing_in_geojson) == 0) {
#   print("✓ すべての都道府県名がgeojsonファイルと一致しています")
# } else {
#   print("⚠ 不一致の都道府県名があります:")
#   print(paste("人口データにない:", paste(missing_in_population, collapse = ", ")))
#   print(paste("geojsonにない:", paste(missing_in_geojson, collapse = ", ")))
# }

# summary statistics
total_population <- sum(japan_population_2024$population)
print(paste("日本総人口:", format(total_population, big.mark = ","), "人"))
print(paste("平均人口:", format(mean(japan_population_2024$population), big.mark = ","), "人"))
print(paste("最大人口:", format(max(japan_population_2024$population), big.mark = ","), "人 (", 
            japan_population_2024$prefecture[which.max(japan_population_2024$population)], ")"))
print(paste("最小人口:", format(min(japan_population_2024$population), big.mark = ","), "人 (", 
            japan_population_2024$prefecture[which.min(japan_population_2024$population)], ")"))

# =============================================================================
# report.Rmdで使用するためのサンプルコード例
# =============================================================================

# 1. 人口データの基本使用例
# source("japan_population_2024.R")  # 人口データを読み込み
# 
# # 2. 受講者数と人口の比較分析例
# # 都道府県別受講者数を集計後、以下のように結合
# # prefecture_summary <- df %>%
# #   group_by(勤務先都道府県) %>%
# #   summarise(受講者数 = n()) %>%
# #   left_join(japan_population_2024, by = c("勤務先都道府県" = "prefecture")) %>%
# #   mutate(
# #     受講率_per_10万人 = (受講者数 / population) * 100000,
# #     人口カテゴリ = case_when(
# #       population >= 5000000 ~ "大都市圏",
# #       population >= 1000000 ~ "中規模県",
# #       TRUE ~ "小規模県"
# #     )
# #   )
#
# # 3. 地図データとの結合例（sfパッケージ使用）
# # library(sf)
# # geojson_data <- st_read("japan.geojson")
# # map_data <- geojson_data %>%
# #   left_join(japan_population_2024, by = c("nam_ja" = "prefecture"))
#
# # 4. 人口密度の計算例（面積データがある場合）
# # japan_population_2024 <- japan_population_2024 %>%
# #   mutate(
# #     人口密度 = population / 面積_km2,  # 面積データが必要
# #     人口規模 = cut(population, 
# #                    breaks = c(0, 1000000, 3000000, 5000000, Inf),
# #                    labels = c("100万人未満", "100-300万人", "300-500万人", "500万人以上"))
# #   )